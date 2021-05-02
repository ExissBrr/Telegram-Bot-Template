from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.database_api.schemes.user import DBCommandsUser
from utils.misc import get_user_id


class GetUserFromDatabase(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):
        user_id = get_user_id(message)
        user = await DBCommandsUser.get_user(id=user_id)
        data["user"] = user

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        user_id = get_user_id(call)
        user = await DBCommandsUser.get_user(id=user_id)
        data["user"] = user
