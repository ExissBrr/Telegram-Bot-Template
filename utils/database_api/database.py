from typing import List

import sqlalchemy as sa
from loguru import logger
from sqlalchemy import DateTime, Column
from sqlalchemy.sql import Select

from data.config import PG_URL
from loader import DATABASE


class BaseModel(DATABASE.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"

    query: Select

    async def update(self, **kwargs):
        """
        Обновляет данные полей таблицы в базе данных
        :param kwargs: Поля в таблице и новое значение
        :return:
        """
        await self.update(**kwargs).apply()


class TimedBaseModel(BaseModel):
    __abstract__ = True

    create_at = Column(DateTime(True), server_default=DATABASE.func.now())
    update_at = Column(DateTime(True), default=DATABASE.func.now(), onupdate=DATABASE.func.now(), server_default=DATABASE.func.now())

async def connect():
    """Подключение к базе данных"""
    logger.info("Database connect")
    await DATABASE.set_bind(bind=PG_URL)
    logger.success("Database connected")



async def unconnect():
    """Отключение от базы данных"""
    logger.info("Database unconnect")
    DATABASE.pop_bind()
    logger.success("Database unconnected")



async def create_tables():
    """Создание таблиц"""
    logger.info("Tables create")
    await DATABASE.gino.create_all()
    logger.success("Tables created")



async def drop_tables():
    """Очистка таблиц"""
    await DATABASE.gino.drop_all()
    logger.warning("Tables drop")
