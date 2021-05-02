import loguru
from loguru import logger
from sqlalchemy import Column, BigInteger, String, Boolean
from sqlalchemy.sql.elements import and_, or_

from utils.database_api.database import TimedBaseModel


class User(TimedBaseModel):
    """
    Объект пользователя из таблицы базы данных
    """
    __tablename__ = "Users"

    id: int = Column(BigInteger, primary_key=True)
    full_name: str = Column(String(200))
    username: str = Column(String(100))

    status_blocked: bool = Column(Boolean, default=False)
    status_active: bool = Column(Boolean, default=True)

    @property
    def is_blocked(self) -> bool:
        """Возвращает статус блокировки пользователя"""
        return self.status_blocked

    @property
    def is_active(self) -> bool:
        """Возвращает статус активности пользователя"""
        return self.status_active

    async def update_status_blocked(self, new_status: bool):
        """
        Обновляет статус блокировки у пользователя
        :param new_status: Новый статус пользователя, на который нужно заменить
        """
        await self.update(status_blocked=new_status)

    async def update_status_active(self, new_status: bool):
        """
        Обновляет статус активности у пользователя
        :param new_status: Новый статус пользователя, на который нужно заменить
        """
        await self.update(status_active=new_status)


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
    @logger.catch
    async def is_user(**kwargs):
        user = await User.query.where(make_filter(**kwargs)).gino.first()
        return bool(user)

    @staticmethod
    @logger.catch
    async def get_user(**kwargs):
        user = await User.query.where(make_filter(**kwargs)).gino.first()
        logger.success(f"Retrieved user from database {kwargs}")
        return user

    @staticmethod
    @logger.catch
    async def get_users(**kwargs):
        users = await User.query.where(make_filter(**kwargs)).gino.all()
        logger.success(f"Retrieved users from database {kwargs}")
        return users

    @staticmethod
    @logger.catch
    async def get_count_users(**kwargs):
        total = len(await DBCommandsUser.get_users(**kwargs))
        return total


def make_filter(
        operator: str = "AND",
        id: int = None,
        status_blocked: bool = None,
        status_active: bool = None
):
    """Формирует фильтр для запроса в таблицу
    :param operator: OR: или, ADN: и
    :param id: Уникальный id пользователя
    :param status_blocked: Статус блокировки
    :param status_active: Статус активности
    :return:
    """
    conditions = []
    if id is not None:
        conditions.append(User.id == id)

    if status_blocked is not None:
        conditions.append(User.status_blocked == status_blocked)

    if status_active is not None:
        conditions.append(User.status_active == status_active)

    if operator == "AND":
        return and_(*conditions)
    elif operator == "OR":
        return or_(*conditions)
