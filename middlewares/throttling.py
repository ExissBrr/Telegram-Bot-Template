import datetime as dt
from asyncio import sleep

from aiogram import types, Dispatcher
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from loguru import logger

from data import text_template
from data.config import TIMEZONE, TIME_MUTE


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit: float = 0, key_prefix: str = "antiflood_"):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.limit
            key = f"{self.key}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as throttled:
            await self.message_throttled(message, throttled)

    async def message_throttled(self, message: types.Message, throttled: Throttled):

        if 4 <= throttled.exceeded_count <= 7:
            await message.answer(text_template.default.warning_rate_limit)
            return True
        elif throttled.exceeded_count == 8:
            await message.answer(
                text=text_template.default.mute
            )
            raise CancelHandler()
        elif throttled.exceeded_count > 8:
            raise CancelHandler()