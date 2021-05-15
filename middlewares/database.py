from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from utils.database_api.models.user import DBCommandsUser
from utils.parse_data.user import get_user_id


class GetUserFromDatabase(BaseMiddleware):

    async def on_process_message(self, message: Message, data: dict):
        user_id = get_user_id(message)
        user = await DBCommandsUser.get_user(id=user_id)
        data["user"] = user

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        user_id = get_user_id(call)
        user = await DBCommandsUser.get_user(id=user_id)
        data["user"] = user
