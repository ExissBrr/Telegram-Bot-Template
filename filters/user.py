from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS_ID
from utils.database_api.schemes.user import DBCommandsUser, UserRankType
from utils.parse_data.user import get_user_id


class Admin(BoundFilter):
    """Фильтр на админа"""

    async def check(self, obj: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(obj)

        return user_id in ADMINS_ID or await DBCommandsUser.is_user(id=user_id, rank=UserRankType.ADMIN)


class NotAdmin(BoundFilter):
    """Фильтр на админа"""

    async def check(self, obj: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(obj)
        return not(user_id in ADMINS_ID or await DBCommandsUser.is_user(id=user_id, rank=UserRankType.ADMIN))


class NewUser(BoundFilter):

    async def check(self, obj: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(obj)
        return not(await DBCommandsUser.is_user(id=user_id))


class NotNewUser(BoundFilter):

    async def check(self, obj: Union[types.Message, types.CallbackQuery]):
        user_id = get_user_id(obj)
        return await DBCommandsUser.is_user(id=user_id)

class Blocked(BoundFilter):
    """Пользователь заблокирован"""

    async def check(self, obj: Union[types.Message, types.CallbackQuery]) -> bool:
        user_id = get_user_id(obj)
        user = await DBCommandsUser.get_user(id=user_id)
        return user.is_blocked


class NotBlocked(BoundFilter):
    """Пользователь заблокирован"""

    async def check(self, obj: Union[types.Message, types.CallbackQuery]) -> bool:
        user_id = get_user_id(obj)
        user = await DBCommandsUser.get_user(id=user_id)
        return user.is_blocked
