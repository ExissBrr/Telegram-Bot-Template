from loader import DP
from .database import GetUserFromDatabase
from .throttling import ThrottlingMiddleware

if __name__ == 'middlewares':
    DP.middleware.setup(ThrottlingMiddleware())
    DP.middleware.setup(GetUserFromDatabase())
