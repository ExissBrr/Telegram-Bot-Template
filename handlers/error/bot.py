from aiogram import types
from loguru import logger

from loader import dp
from utils.notify.users import send_messages


@dp.errors_handler()
async def errors_logging(update: types.Update, exception):
    """
    Обработчик ошибок, вызванных самим ботом
    :param update: Апдейт, где произошла ошибка
    :param exception: Ошибка
    :return:
    """
    try:
        logger.error(f"Error {exception}: {exception.match}.")

        await send_messages(exception.match, debug=True)

    except AttributeError as err:
        try:
            logger.error(f"Error {exception}: {exception.text}.")

            await send_messages(exception.text, debug=True)

        except AttributeError as err:
            logger.error(f"Error {exception}.")

            await send_messages(exception, debug=True)
