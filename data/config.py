import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT: str = os.getenv("TOKEN_BOT")

ADMINS_ID: List[int] = list(map(int, (os.getenv("ADMINS_ID").split())))
DEVELOPERS_ID: List[int] = list(map(int, (os.getenv("DEVELOPERS_ID").split())))


PG_USER: str = os.getenv('PG_USER')
PG_PASS: str = os.getenv('PG_PASS')
DATABASE: str = os.getenv('DATABASE')
IP: str = os.getenv("IP")
PG_URL = f'postgresql://{PG_USER}:{PG_PASS}@{IP}/{DATABASE}'

# В секундах
DEFAULT_RATE_LIMIT = 0.4

# Глубина реферальной системы
DEFAULT_LEVEL_REFERRAL_SYSTEM = 1
