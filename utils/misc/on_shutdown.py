from aiogram import Dispatcher
from loguru import logger

from utils.database_api import database
from utils.database_api.models.user import UserRole
from utils.notify import users


async def on_shutdown(dispatcher: Dispatcher):
    """
    Выполняется при завершении работы бота.
    :return:
    """

    # Рассылка сообщений администраторам.
    await users.send_messages("Бот Выключен!", role=UserRole.ADMIN)

    # Отключение от базы данных.
    await database.unconnect()

    # Удаление команд бота
    await dispatcher.bot.set_my_commands([])

    logger.info("Bot is disabled")
