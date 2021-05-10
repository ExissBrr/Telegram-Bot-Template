from typing import Union, List

from aiogram import types

from data.config import DEFAULT_LEVEL_REFERRAL_SYSTEM
from exeptions.data import FailedGetUserId
from utils.database_api.schemes.user import DBCommandsUser, User


def get_user_id(data: Union[str, int, types.Message, types.CallbackQuery]):
    """
    Возвращает из события id пользователя
    :param data: Событие из бота
    :return: id пользователя
    """
    if isinstance(data, str):
        return int(data)

    if isinstance(data, int):
        return data

    if isinstance(data, types.Message):
        return data.from_user.id

    if isinstance(data, types.CallbackQuery):
        return data.message.chat.id

    raise FailedGetUserId(data)


async def get_referrals(user_id: int, referrals: list, levels: int = DEFAULT_LEVEL_REFERRAL_SYSTEM) -> List[User]:
    """Возвращает список рефералов по ветке
    :param user_id: id пользователя, чью ветку вернуть
    :param levels: глубина ветки
    :param referrals: список рефералов в ветке(Для рекурсии)
    :return: Возвращает список пользователей

    :warning В referrals передать пустой список
    """

    user = await DBCommandsUser.get_user(user_id=user_id)

    if user.is_referral and await DBCommandsUser.is_user(user_id=user_id) and levels > 0:
        referral = await DBCommandsUser.get_user(user_id=user.referral_id)
        referrals.append(referral)
        referrals = await get_referrals(referral.id, referrals, levels-1,)

    return referrals

