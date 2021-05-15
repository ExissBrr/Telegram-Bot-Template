from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS_ID
from utils.database_api.models.user import DBCommandsUser, UserRole
from utils.parse_data.user import get_user_id


class Admin(BoundFilter):
    """Фильтр на админа"""

    async def check(self, obj: Union[Message, CallbackQuery]):
        user_id = get_user_id(obj)

        return user_id in ADMINS_ID or await DBCommandsUser.is_user(id=user_id, role=UserRole.ADMIN)


class NewUser(BoundFilter):
    """Фильтр на пользователя, которого нет в базе данных"""

    async def check(self, obj: Union[Message, CallbackQuery]):
        user_id = get_user_id(obj)
        return not (await DBCommandsUser.is_user(id=user_id))


class NotNewUser(BoundFilter):
    """Фильтр на пользователя, который есть в базе данных"""

    async def check(self, obj: Union[Message, CallbackQuery]):
        user_id = get_user_id(obj)
        return await DBCommandsUser.is_user(id=user_id)


class Blocked(BoundFilter):
    """Фильтр на заблокированного пользователя"""

    async def check(self, obj: Union[Message, CallbackQuery]) -> bool:
        user_id = get_user_id(obj)

        if not await DBCommandsUser.is_user(id=user_id):
            return False

        user = await DBCommandsUser.get_user(id=user_id)
        return user.is_blocked
