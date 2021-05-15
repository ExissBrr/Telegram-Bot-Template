from asyncio import sleep

from aiogram import Dispatcher
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from aiogram.utils.exceptions import Throttled

from data import text


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit: float = 0, key_prefix: str = "antiflood_"):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict):
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

            raise CancelHandler()

    async def message_throttled(self, message: Message, throttled: Throttled):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()

        delta = throttled.rate - throttled.delta
        if handler:
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            key = f"{self.key}_message"

        if throttled.exceeded_count <= 2:
            await message.reply(text=text.message.default.warning_mute)

        await sleep(delta)

        throttled_tmp = await dispatcher.check_key(key)

        if throttled_tmp.exceeded_count == throttled.exceeded_count:
            await message.answer(text.message.default.notification_unmute)
