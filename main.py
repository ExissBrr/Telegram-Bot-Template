from aiogram.utils import executor

from utils.misc import on_startup, on_shutdown


def main():
    """
    Главная функция.
    :return:
    """
    import handlers
    import middlewares
    import utils

    __all__ = ["handlers", "middlewares", "utils"]

    executor.start_polling(handlers.dp, on_startup=on_startup, on_shutdown=on_shutdown)

if __name__ == '__main__':
    main()