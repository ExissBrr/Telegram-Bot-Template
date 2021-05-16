
from loguru import logger

from data.config import PG_URL
from loader import database


class Database:

    @staticmethod
    async def create_bind():
        """Подключение к базе данных"""
        logger.info("Database connect")
        await database.set_bind(bind=PG_URL)
        logger.success("Database connected")

    @staticmethod
    async def pop_bind():
        """Отключение от базы данных"""
        logger.info("Database unconnect")
        await database.pop_bind()
        logger.success("Database unconnected")

    @staticmethod
    async def create_tables():
        """Создание таблиц"""
        logger.info("Tables create")
        await database.gino.create_all()
        logger.success("Tables created")

    @staticmethod
    async def drop_tables():
        """Очистка таблиц"""
        await database.gino.drop_all()
        logger.warning("Tables drop")
