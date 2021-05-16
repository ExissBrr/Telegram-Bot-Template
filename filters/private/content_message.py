from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class NotCommandStart(BoundFilter):
    """Не является ли сообщение командой старт"""

    async def check(self, message: Message):
        return not ("start" in message.text.lower())
