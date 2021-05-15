from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import text
from filters.private.role_user import Admin, NewUser
from keyboards import reply
from loader import DP
from utils.database_api.models.user import DBCommandsUser, UserRole


@DP.message_handler(Admin(), CommandStart(), NewUser())
async def add_admin_in_db(message: types.Message):
    """Добавление админа в базу данных"""
    await DBCommandsUser.add_user(
        id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        role=UserRole.ADMIN
    )
    await message.answer(
        text=text.message.admin.command_start,
        reply_markup=reply.admin.start.keyboard
    )
