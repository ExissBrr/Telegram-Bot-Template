from aiogram import Dispatcher
from loguru import logger

from utils.database_api.database import Database
from utils.database_api.models.user import UserRole
from utils.misc import set_bot_commands
from utils.notify import users


async def on_startup(dispatcher: Dispatcher):
    """
    Выполняется при запуске бота.
    :return:
    """
    logger.info("Start pulling")

    # Установка команд в боте.
    await set_bot_commands(dispatcher)

    # Подключение к базе данных.
    await Database.create_bind()

    # TODO: При коммите комментировать! Иначе все данные в таблицах сотрутся.
    # await Database.drop_tables()

    # Создание таблиц.
    await Database.create_tables()

    # Рассылка сообщений администраторам.
    await users.send_messages("Бот Включен!", role=UserRole.ADMIN)

