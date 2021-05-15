from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from data import text
from keyboards import reply
from utils.database_api.models.user import DBCommandsUser
from utils.parse_data.user import get_user_id


async def main_auto(message: Message, state: FSMContext = None):
    if state:
        await state.finish()

    user_id = get_user_id(message)
    user = await DBCommandsUser.get_user(id=user_id)

    if user.is_admin:
        await message.answer(
            text=text.message.send_main_keyboard,
            reply_markup=reply.admin.start.keyboard
        )
    else:
        await message.answer(
            text=text.message.send_main_keyboard,
            reply_markup=reply.default.start.keyboard
        )

send_main_keyboard