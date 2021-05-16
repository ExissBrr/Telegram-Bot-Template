from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from gino import Gino

from data.config import TOKEN_BOT

database = Gino()
storage = MemoryStorage()
bot = Bot(token=TOKEN_BOT, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)

__all__ = ["storage", "bot", "dp", "database"]


