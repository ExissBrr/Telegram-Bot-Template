from aiogram import types

from data.config import DEFAULT_RATE_LIMIT
from filters.user import Admin
from keyboards import reply
from loader import DP
from utils.database_api.schemes.user import User

from utils.misc import rate_limit


@rate_limit(DEFAULT_RATE_LIMIT)
@DP.message_handler(content_types=types.ContentTypes.ANY)
async def send_main_keyboard_user(message: types.Message, user: User):
    """Выдача главной клавиатуры пользователю, в зависимости от его должности клавиатуры."""

    if user.is_admin:
        await message.answer(
            text="Выдана клавиатура",
            reply_markup=reply.admin.start.keyboard
        )
    else:
        await message.answer(
            text="Выдана клавиатура",
            reply_markup=reply.default.start.keyboard
        )
