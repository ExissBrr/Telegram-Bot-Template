from aiogram import types
from loguru import logger

from loader import DP


@DP.errors_handler()
async def errors_logging(update: types.Update, exception):
    """
    Обработчик ошибок, вызванных самим ботом
    :param update: Апдейт, где произошла ошибка
    :param exception: Ошибка
    :return:
    """

    logger.error(f"Error {exception}: {exception.match}.")



