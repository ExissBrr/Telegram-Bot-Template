from typing import Union

from aiogram import types


def get_user_id(event: Union[types.Message, types.CallbackQuery]):
    """
    Возвращает из события id пользователя
    :param event: Событие из бота
    :return: id пользователя
    """
    if isinstance(event, types.Message):
        return event.from_user.id

    if isinstance(event, types.CallbackQuery):
        return event.message.chat.id

