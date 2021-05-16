from aiogram import types

from data.config import DEFAULT_RATE_LIMIT
from loader import dp
from utils.misc import rate_limit, send_keyboard


@rate_limit(DEFAULT_RATE_LIMIT)
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def send_main_keyboard_user(message: types.Message):
    """Выдача главной клавиатуры пользователю, в зависимости от его должности клавиатуры."""

    await send_keyboard.main_auto(message)
