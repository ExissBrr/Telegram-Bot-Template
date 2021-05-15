from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class NotPrivate(BoundFilter):
    """Фильтр на диалог не в приватно чате"""

    async def check(self, message: Message):
        return not (message.chat.type == "private")
