from aiogram import Dispatcher
from aiogram.types import BotCommand
from loguru import logger

commands = {
    "/help": "Получить справочник.",
    "/settings": "Настройки аккаунта",
    "/start": "Получить клавиатуру|Начать диалог.",
}


async def set_bot_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands(
        commands=[
            BotCommand(
                command, description
            ) for command, description in commands.items()
        ]
    )
    logger.info("Installed bot commands")
