from aiogram import types
from loguru import logger

from loader import DP
from utils.database_api.schemes.user import User
from utils.misc import rate_limit


@rate_limit(1)
@DP.message_handler(content_types=types.ContentTypes.ANY)
async def send_keyboard_user(message: types.Message, user: User):
    await message.answer("Мяу")

