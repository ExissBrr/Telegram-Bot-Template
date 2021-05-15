from aiogram import types

from data.config import DEFAULT_RATE_LIMIT
from keyboards import reply
from loader import DP
from utils.database_api.models.user import User

from utils.misc import rate_limit, send_keyboard


@rate_limit(DEFAULT_RATE_LIMIT)
@DP.message_handler(content_types=types.ContentTypes.ANY)
async def send_main_keyboard_user(message: types.Message):
    """Выдача главной клавиатуры пользователю, в зависимости от его должности клавиатуры."""

    await send_keyboard.main_auto(message)
