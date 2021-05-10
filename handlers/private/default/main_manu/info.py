from aiogram import types

from data import button_text, text_template
from loader import DP
from utils.misc import rate_limit


@rate_limit(1.5)
@DP.message_handler(text=button_text.navigation.INFO)
async def send_info_menu(message: types.Message):
    """Отправка информационного меню пользователю."""
    await message.answer(
        text=text_template.default.info
    )
