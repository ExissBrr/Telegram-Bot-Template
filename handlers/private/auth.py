from aiogram import types

from filters.content_message import NotCommandStart
from filters.user import NewUser
from loader import DP


@DP.message_handler(NewUser(), NotCommandStart())
async def notify_not_user_in_database(message: types.Message):
    """Уведомляет пользователя, что его нет в базе данных."""
    await message.answer(
        text="Упс, я не нашел вас в своей базе данных, пропишите /start"
    )