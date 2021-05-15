from aiogram.types import Message

from data import text
from data.config import DEFAULT_RATE_LIMIT
from filters.private.content_message import NotCommandStart
from filters.private.filter import NotPrivate
from filters.private.role_user import Blocked, NewUser
from loader import DP
from utils.database_api.models.user import User
from utils.misc import rate_limit


@DP.message_handler(NotPrivate())
async def filter_not_chat_private(message: Message):
    pass


@rate_limit(120)
@DP.message_handler(Blocked())
async def notify_blocked(message: Message, user: User):
    bot_data = await DP.bot.get_me()
    await message.answer(
        text=text.message.default.warning_blocked.format(
            bot_username=bot_data.username,
            user_username=user.username,
            user_full_name=user.full_name,
            user_id=user.id,
            blocking_time=user.update_at,
            report_block=user.report_block,
        )
    )


@rate_limit(DEFAULT_RATE_LIMIT)
@DP.message_handler(NewUser(), NotCommandStart())
async def notify_not_user_in_database(message: Message):
    """Уведомляет пользователя, что его нет в базе данных."""
    await message.answer(
        text=text.message.notification_not_user_in_database
    )
