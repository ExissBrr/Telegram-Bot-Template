from aiogram import Dispatcher
from loguru import logger

from utils.database_api import database
from utils.notify import admins


async def on_startup(dispatcher: Dispatcher):
    """
    Выполняется при запуске бота
    :return:
    """
    logger.info("Start pulling")
    # Рассылка сообщений администраторам
    await admins.send_messages("Бот Включен!")

    # Подключение к базе данных
    await database.connect()

    # TODO: При коммите комментировать! Иначе все данные в таблицах сотрутся
    await database.drop_tables()

    # Создание таблиц
    await database.create_tables()

