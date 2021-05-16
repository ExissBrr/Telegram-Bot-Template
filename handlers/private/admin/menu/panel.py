from aiogram.types import Message

from data import text
from filters.private.role_user import Admin
from loader import dp
from utils.database_api.models.user import DBCommandsUser


@dp.message_handler(Admin(), text=text.button.reply.admin.menu_panel)
async def send_admin_menu_panel(message: Message):
    """Отравляет панель администратору"""
    await message.answer(
        text=text.message.admin.menu_panel.format(
            count_users_in_db=await DBCommandsUser.get_count(),
            count_active_users=await DBCommandsUser.get_count(is_active=True),
            count_users_blocked=await DBCommandsUser.get_count(is_blocked=True),
            count_users_referred=await DBCommandsUser.get_count(is_referred=True),
        )
    )