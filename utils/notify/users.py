from aiogram import types
from loguru import logger

from data.config import DEVELOPERS_ID
from loader import BOT
from utils.database_api.models.user import DBCommandsUser, UserRole


async def send_copy_messages(message: types.Message, debug: bool = False, **kwargs):
    """
    Рассылка копии сообщения пользователям
    :param message: Сообщение, копию которого нужно разослать
    :param debug: Дебаг режим. True - информация придет только разработчикам бота
    :return:
    """
    logger.info(f'Notify users. Chat id: {message.from_user.id} Message id: "{message.message_id}". Debug: {debug}. Filters: {kwargs}')
    if debug:
        for user_id in DEVELOPERS_ID:
            try:
                await BOT.copy_message(user_id, message_id=message.message_id)
            except Exception as err:
                logger.error(f"ERROR {err}. Пользователю с ID {user_id} не удалось доставить "
                             f"копию сообщения с id {message.message_id} "
                             f"из чата {message.from_user.id}")

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


async def send_messages(text: str, debug: bool = False, **kwargs):
    """
    Рассылка текста пользователям
    :param text: Текст рассылки
    :param debug: Дебаг режим. True - информация придет только разработчикам бота
    :return:
    """
    logger.info(f'Notify users. Message text: "{text}". Debug: {debug}. Filters: {kwargs}')

    if debug:
        for user_id in DEVELOPERS_ID:
            try:
                await BOT.send_message(user_id, text=text)

            except Exception as err:
                logger.error(f"ERROR {err}. Пользователю с ID {user_id} не удалось доставить сообщение: {text}.")
        return

    users = await DBCommandsUser.get_users(**kwargs)
    for user in users:
        try:
            await BOT.send_message(chat_id=user.id, text=text)
        except Exception as err:

            # Пользователь помечается в базе, как пассивный
            await user.update_rank(UserRole.PASSIVE)

            logger.error(f"ERROR {err}. Пользователю с ID {user.id} не удалось доставить сообщение: {text}.")
