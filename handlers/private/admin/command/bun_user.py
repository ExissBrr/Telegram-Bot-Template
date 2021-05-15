from aiogram import types
from aiogram.dispatcher.filters import Command
from loguru import logger

from filters.private.role_user import Admin
from loader import DP
from utils.database_api.models.user import DBCommandsUser, UserRole
from utils.parse_data.user import get_user_id


@DP.message_handler(Admin(), Command("bun"))
async def block_user(message: types.Message):
    try:
        data = message.get_args().split()
        user_id = get_user_id(data[0])
        if len(data) > 1:
            report = ' '.join(data[1:])
        else:
            report = 'Не указана'
    except Exception as err:
        await message.answer("Ошибка! Попробуйте снова!")
        logger.error(err)
        return False

    if not await DBCommandsUser.is_user(id=user_id):
        await message.answer("Пользователь не найден")
        return False

    user = await DBCommandsUser.get_user(id=user_id)

    if user.is_blocked:
        await message.answer("Пользователь уже находится в блокировке")
        return False
    elif user.role is UserRole.ADMIN:
        await message.answer("Пользователей с правами Администратора блокировать нельзя")
        return False

    await user.update_rank(UserRole.BLOCKED)
    await user.update_report_block(report)

    await message.answer("Пользователь заблокирован")
