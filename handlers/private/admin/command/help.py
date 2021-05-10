from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from data import text_template
from filters.user import Admin
from keyboards import reply
from loader import DP


@DP.message_handler(Admin(), CommandHelp())
async def send_help_menu(message: types.Message):
    """Отправка справочника пользователю"""
    await message.answer(
        text=text_template.admin.help,
        reply_markup=reply.admin.start.keyboard
    )
