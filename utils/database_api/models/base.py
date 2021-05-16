from typing import List

import sqlalchemy as sa
from loguru import logger
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import Select

from loader import database


class BaseModel(database.Model):
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

    async def update_data(self, **kwargs) -> object:
        """
        Обновляет данные полей таблицы в базе данных
        :param kwargs: Поля в таблице и новое значение
        :return:
        """
        await self.update(**kwargs).apply()
        logger.success(f"{self.__tablename__} (id: {self.id}) set new param {kwargs}")


class TimedBaseModel(BaseModel):
    __abstract__ = True

    create_at = Column(DateTime(True), server_default=database.func.now())
    update_at = Column(DateTime(True), default=database.func.now(), onupdate=database.func.now(),
                       server_default=database.func.now())
