from loguru import logger

from data.config import ADMINS_ID
from loader import BOT


async def send_messages(message: str):
    """
    Рассылка сообщений админ-команде
    :param message:
    :return:
    """
    logger.info(f'Notify admins. Message: "{message}" ')
    try:
        for admin_id in ADMINS_ID:
            await BOT.send_message(admin_id, message)
    except Exception as err:
        logger.error(f'Администратору с ID {admin_id} не удалось доставить сообщение: "{message}". Ошибка: {err}')
