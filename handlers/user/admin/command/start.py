from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import text_template
from filters.user import IsAdmin, IsNewUser, IsNotNewUser
from loader import DP
from utils.database_api.schemes.user import DBCommandsUser
from utils.misc import rate_limit


@DP.message_handler(CommandStart(), IsAdmin(), IsNewUser())
async def on_message(message: types.Message):
    """Логика на команду старт"""
    await DBCommandsUser.add_user(
        id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username
    )
    await message.answer(text_template.admin.welcome)


@rate_limit(limit=0.4)
@DP.message_handler(CommandStart(), IsAdmin(), IsNotNewUser())
async def on_message(message: types.Message):
    """Логика на команду старт"""
    await message.answer(
        """Выдана клавиатура для администрации"""
    )