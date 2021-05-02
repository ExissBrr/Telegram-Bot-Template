from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import text_template
from filters.user import IsNewUser, IsNotNewUser
from loader import DP
from utils.database_api.schemes.user import DBCommandsUser


@DP.message_handler(CommandStart(), IsNewUser())
async def on_message(message: types.Message):
    """Логика на команду старт для новых пользователей"""
    await DBCommandsUser.add_user(
        id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username
    )

    await message.answer(
        text_template.default.welcome.format(
            user_full_name=message.from_user.full_name
        )
    )


@DP.message_handler(CommandStart(), IsNotNewUser())
async def on_message(message: types.Message):
    """Логика на команду старт для новых пользователей"""
    bot = message.bot.get_me()
    await message.answer(
        f"Вы уже зарегистрированы в боте {bot.username}"
    )