from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS_ID
from utils.database_api.schemes.user import DBCommandsUser
from utils.misc.get_user_id import get_user_id


class IsAdmin(BoundFilter):
    """Фильтр на админа"""

    async def check(self, event: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(event)
        return user_id in ADMINS_ID


class IsNotAdmin(BoundFilter):
    """Фильтр на админа"""

    async def check(self, event: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(event)
        return not(user_id in ADMINS_ID)


class IsNewUser(BoundFilter):

    async def check(self, event: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(event)
        return not(await DBCommandsUser.is_user(id=user_id))


class IsNotNewUser(BoundFilter):

    async def check(self, event: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(event)
        return await DBCommandsUser.is_user(id=user_id)