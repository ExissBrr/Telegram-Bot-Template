from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data import text, link
from data.config import DEFAULT_RATE_LIMIT
from filters.private.role_user import NewUser
from keyboards import reply
from loader import DP
from utils.database_api.models.user import DBCommandsUser, UserRole
from utils.misc import rate_limit


@rate_limit(DEFAULT_RATE_LIMIT)
@DP.message_handler(CommandStart(), NewUser())
async def add_user_in_db(message: types.Message):
    """Добавление пользователя в базу данных."""
    referral_id = 0 or message.get_args()

    if referral_id and await DBCommandsUser.is_user(referral_id):
        referral_id = int(referral_id)

    await DBCommandsUser.add_user(
        id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        referral_id=referral_id
    )

    await message.answer_photo(
        photo=link.photo.TEMPLATE,
        caption=text.message.default.command_start.format(
            user_full_name=message.from_user.full_name
        ),
        reply_markup=reply.default.start.keyboard
    )