from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import text_template
from filters.user import Admin, NewUser, NotNewUser
from keyboards import reply
from loader import DP
from utils.database_api.schemes.user import DBCommandsUser, UserRankType
from utils.misc import rate_limit


@DP.message_handler(CommandStart(), Admin(), NewUser())
async def add_admin_in_db(message: types.Message):
    """Добавление админа в базу данных"""
    await DBCommandsUser.add_user(
        id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        rank=UserRankType.ADMIN
    )
    await message.answer(
        text_template.admin.welcome,
        reply_markup=reply.admin.start.keyboard
    )


@DP.message_handler(CommandStart(), Admin(), NotNewUser())
async def on_message(message: types.Message):
    """Выдача клавиатуры администратору"""
    await message.answer(
        "Вы уже зарегистрированы.",
        reply_markup=reply.admin.start.keyboard
    )