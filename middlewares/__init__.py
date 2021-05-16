from loader import dp
from .database import GetUserFromDatabase
from .throttling import ThrottlingMiddleware

if __name__ == 'middlewares':
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(GetUserFromDatabase())
