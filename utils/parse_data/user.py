from typing import Union

from aiogram import types


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
