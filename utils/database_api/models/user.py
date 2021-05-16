from typing import List

from loguru import logger
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.sql.elements import and_, or_

from utils.database_api.models.base import TimedBaseModel


class UserRole:
    """Типы ролей пользователей"""

    ADMIN = 1
    DEFAULT = 2
    PASSIVE = 3
    BLOCKED = 4


class User(TimedBaseModel):
    """
    Объект пользователя из таблицы базы данных
    """
    __tablename__ = "Users"

    id: int = Column(BigInteger, primary_key=True)
    full_name: str = Column(String(200))
    username: str = Column(String(100), default='-')

    referral_id: int = Column(BigInteger, default=0)

    role: str = Column(BigInteger, default=UserRole.DEFAULT)

    report_block: str = Column(String(200), default="Не указано")

    @property
    def is_blocked(self) -> bool:
        """Возвращает статус блокировки пользователя"""
        return self.role == UserRole.BLOCKED

    @property
    def is_active(self) -> bool:
        """Возвращает статус активности пользователя"""
        return self.role == UserRole.PASSIVE

    @property
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN

    @property
    def is_referred(self) -> bool:
        return bool(self.referral_id)


    async def update_role(self, new_role: str) -> str:
        """
        Обновляет уровень привилегий у пользователя.
        :warning: Используйте class UserRankType для установки уровня
        :param new_role: Новый статус пользователя, на который нужно заменить
        """
        await self.update_data(role=new_role)
        return new_role

    async def update_report_block(self, text: str) -> str:
        """
        Обновляет причину блокировки пользователя
        :param text: Текст причины блокировки
        """
        await self.update_data(report_block=text)
        return text


class DBCommandsUser:

    @staticmethod
    @logger.catch
    async def add_user(**kwargs) -> User:
        """
        Добавление пользователя в таблицу
        :param kwargs:
        :keyword id:
        :keyword full_name:
        :keyword username:
        :return: объект созданного пользователя
        """
        user = User(**kwargs)
        try:
            await user.create()
            logger.success(f"Created new user {kwargs}")
            return user
        except Exception as err:
            logger.error(f"Failed to create new user {kwargs}. Error: {err}")

    @staticmethod
    async def is_user(**kwargs) -> bool:
        """Есть ли пользователя в базе данных"""
        user = await DBCommandsUser.get_user(**kwargs)
        return bool(user)

    @staticmethod
    async def get_user(**kwargs) -> User:
        """Возвращает пользователя из таблицы"""
        user = await User.query.where(make_filter(**kwargs)).gino.first()
        logger.info(f"Retrieved user from database {kwargs}")
        return user

    @staticmethod
    async def get_users(**kwargs) -> List[User]:
        """Возвращает список из объектов пользователей"""
        users = await User.query.where(make_filter(**kwargs)).gino.all()
        logger.info(f"Retrieved users from database {kwargs}")
        return users

    @staticmethod
    async def get_count(**kwargs) -> int:
        """Возвращает кол-во пользователей"""
        total = len(await DBCommandsUser.get_users(**kwargs))
        return total


def make_filter(
        operator: str = "AND",
        id: int = None,
        role: int = None,
        full_name: str = None,
        username: str = None,
        report_block: str = None,
        is_referred: bool = None,
        is_active: bool = None,
        is_blocked: bool = None,
):
    """Формирует фильтр для запроса в таблицу
    :param operator: OR: или, ADN: и
    :param id: Уникальный id пользователя
    :param role: Уровень привилегий пользователя
    :param full_name:
    :param username:
    :param report_block:
    :param is_referred:
    :param is_active:
    :param is_blocked:
    :return:
    """
    conditions = []
    if id is not None:
        conditions.append(User.id == int(id))

    if role is not None:
        conditions.append(User.role == int(role))

    if full_name is not None:
        conditions.append(User.full_name == full_name)

    if username is not None:
        conditions.append(User.username == username)

    if report_block is not None:
        conditions.append(User.report_block)

    if is_referred is not None:
        if is_referred:
            conditions.append(User.referral_id != 0)
        else:
            conditions.append(User.referral_id == 0)

    if is_active is not None:
        if is_active:
            conditions.append(User.role != UserRole.PASSIVE)
        else:
            conditions.append(User.role == UserRole.PASSIVE)

    if is_blocked is not None:
        if is_blocked:
            conditions.append(User.role != UserRole.BLOCKED)
        else:
            conditions.append(User.role == UserRole.BLOCKED)

    if operator == "AND":
        return and_(*conditions)
    elif operator == "OR":
        return or_(*conditions)
