from aiogram import types
from aiogram.dispatcher.filters import Command
from loguru import logger

from filters.user import Admin
from keyboards import reply
from loader import DP
from utils.database_api.schemes.user import UserRankType, DBCommandsUser
from utils.parse_data.user import get_user_id


@DP.message_handler(Admin(), Command("unbun"))
async def block_user(message: types.Message):
    try:
        data = message.get_args().split()
        user_id = get_user_id(data[0])
    except Exception as err:
        await message.answer("Ошибка! Попробуйте снова!")
        logger.error(err)
        return False

    if not await DBCommandsUser.is_user(id=user_id):
        await message.answer("Пользователь не найден")
        return False

    user = await DBCommandsUser.get_user(id=user_id)

    if not user.is_blocked:
        await message.answer("Пользователь итак разблокирован")
        return False

    await user.update_rank(UserRankType.DEFAULT)
    await message.answer("Пользователь разблокирован")
    await DP.bot.send_message(
        chat_id=user.id,
        text="С вас сняты ограничения",
        reply_markup=reply.default.start.keyboard
    )
