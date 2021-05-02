from aiogram import Dispatcher

from utils.database_api import database
from utils.notify import admins


async def on_shutdown(dispatcher: Dispatcher):
    """
    Выполняется при завершении работы бота
    :return:
    """
    await admins.send_messages("Бот Выключен!")

    await database.unconnect()