import loguru
from aiogram.utils import executor
from aiogram.utils.exceptions import TerminatedByOtherGetUpdates
from loguru import logger

from utils.misc import on_startup, on_shutdown


def main():
    """
    Главная функция.
    :return:
    """
    from handlers import DP
    import utils.misc.logging
    import middlewares

    executor.start_polling(DP, on_startup=on_startup, on_shutdown=on_shutdown)

if __name__ == '__main__':
    main()