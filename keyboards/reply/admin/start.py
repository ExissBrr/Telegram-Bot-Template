from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from data import text

keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text=text.button.admin.reply.menu_panel
            )
        ]
    ]
)
