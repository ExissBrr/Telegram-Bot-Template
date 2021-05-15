from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import text
from keyboards.callback_data import get_user_cd

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=text.button.inline.admin.get_info_user,
                callback_data=get_user_cd.new("user_id")

            ),
        ],
        [],
    ]
)