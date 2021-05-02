from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from gino import Gino

from data.config import TOKEN_BOT

DATABASE = Gino()
STORAGE = MemoryStorage()
BOT = Bot(token=TOKEN_BOT, parse_mode=ParseMode.HTML)
DP = Dispatcher(bot=BOT, storage=STORAGE)

__all__ = ["STORAGE", "BOT", "DP", "DATABASE"]


