from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from data import text
from data.config import DEFAULT_RATE_LIMIT
from keyboards import reply
from loader import dp
from utils.misc import rate_limit

@rate_limit(DEFAULT_RATE_LIMIT)
@dp.message_handler(CommandHelp())
async def send_help_menu(message: types.Message):
    """Отправка справочника пользователю"""
    await message.answer(
        text=text.message.default.command_help,
        reply_markup=reply.default.start.keyboard
    )
