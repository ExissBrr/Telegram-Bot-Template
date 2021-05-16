from aiogram import types

from data import text
from data.config import DEFAULT_RATE_LIMIT
from loader import dp
from utils.misc import rate_limit


@rate_limit(DEFAULT_RATE_LIMIT)
@dp.message_handler(text=text.button.reply.default.menu_info)
async def send_info_menu(message: types.Message):
    """Отправка информационного меню пользователю."""
    await message.answer(
        text=text.message.default.menu_info
    )