from aiogram import types

from data import text_template
from filters.content_message import NotCommandStart
from filters.user import NewUser, Blocked, NotNewUser, NotAdmin
from loader import DP
from utils.database_api.schemes.user import User
from utils.misc import rate_limit


@rate_limit(120)
@DP.message_handler(NotNewUser(), Blocked(), NotAdmin())
async def notify_blocked(message: types.Message, user: User):
    bot_data = await DP.bot.get_me()
    await message.answer(
        text=text_template.default.blocked.format(
            bot_username=bot_data.username,
            user_username=user.username,
            user_full_name=user.full_name,
            user_id=user.id,
            blocking_time=user.update_at,
            report_block=user.report_block,
        )
    )



@DP.message_handler(NewUser(), NotCommandStart())
async def notify_not_user_in_database(message: types.Message):
    """Уведомляет пользователя, что его нет в базе данных."""
    await message.answer(
        text="Упс, я не нашел вас в своей базе данных, пропишите /start"
    )