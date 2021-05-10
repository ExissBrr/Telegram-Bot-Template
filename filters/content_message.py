from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class NotCommandStart(BoundFilter):
    """Фильтр на команду страт"""

    async def check(self, message: types.Message):
        return not ("start" in message.text.lower())