from aiogram import types
from loguru import logger


async def send_messages(message: types.Message):
    """
    Рассылка копии сообщения пользователям
    :param message:
    :return:
    """
    users: list
    try:
        for user in users:
            await message.send_copy(user.id)
    except Exception as err:
        logger.error(f"Пользователю с ID {user.id} не удалось доставить сообщение: {message}. Ошибка: {err}")