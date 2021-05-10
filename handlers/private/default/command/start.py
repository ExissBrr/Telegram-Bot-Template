from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import text_template
from filters.user import NewUser, NotNewUser
from keyboards import reply
from loader import DP
from utils.database_api.schemes.user import DBCommandsUser, UserRankType
from utils.misc import rate_limit


@rate_limit(2)
@DP.message_handler(CommandStart(), NewUser())
async def add_user_in_db(message: types.Message):
    """Добавление пользователя в базу данных."""
    await DBCommandsUser.add_user(
        id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        rank=UserRankType.DEFAULT,
    )

    await message.answer(
        text_template.default.welcome.format(
            user_full_name=message.from_user.full_name
        )
    )

@rate_limit(2)
@DP.message_handler(CommandStart(), NotNewUser())
async def on_message(message: types.Message):
    """Выдана стандартной клавиатуры."""
    bot = await message.bot.get_me()
    await message.answer(
        f"Вы уже зарегистрированы в боте @{bot.username}",
        reply=reply.default.start.keyboard
    )
