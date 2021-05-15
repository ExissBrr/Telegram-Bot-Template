from aiogram import types
from loguru import logger

from loader import BOT
from utils.database_api.models.user import DBCommandsUser, UserRole


async def send_copy_messages(message: types.Message, **kwargs):
    """
    Рассылка копии сообщения пользователям
    :param message:
    :return:
    """
    logger.info(f'Notify users. Chat id: {message.from_user.id} Message id: "{message.message_id}". Filters: {kwargs}')
    users = await DBCommandsUser.get_users(**kwargs)

    for user in users:
        try:
            await message.send_copy(chat_id=user.id)
        except Exception as err:

            # Пользователь помечается в базе, как пассивный
            await user.update_rank(UserRole.PASSIVE)

            logger.error(f"ERROR {err}. Пользователю с ID {user.id} не удалось доставить "
                         f"копию сообщения с id {message.message_id} "
                         f"из чата {message.from_user.id}")


async def send_messages(text: str, **kwargs):
    """
    Рассылка текста пользователям
    :param text:
    :return:
    """

    users = await DBCommandsUser.get_users(**kwargs)

    logger.info(f'Notify users. Message text: "{text}". Filters: {kwargs}')

    for user in users:
        try:
            await BOT.send_message(chat_id=user.id, text=text)
        except Exception as err:

            # Пользователь помечается в базе, как пассивный
            await user.update_rank(UserRole.PASSIVE)

            logger.error(f"ERROR {err}. Пользователю с ID {user.id} не удалось доставить сообщение: {text}.")