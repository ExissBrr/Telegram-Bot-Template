from aiogram import types
from aiogram.dispatcher.filters import CommandSettings

from data import text
from data.config import DEFAULT_RATE_LIMIT
from loader import DP
from utils.misc import rate_limit


@rate_limit(DEFAULT_RATE_LIMIT)
@DP.message_handler(CommandSettings())
async def send_settings_menu(message: types.Message):
    """Отправляет меню настройки аккаунта"""
    await message.answer(
        text=text.message.default.command_settings
    )
