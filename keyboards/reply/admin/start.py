from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from data import button_text

keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text=button_text.navigation.INFO
            )
        ]
    ]
)
