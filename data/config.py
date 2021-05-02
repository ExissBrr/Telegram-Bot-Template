import os
from typing import List

import pytz
from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT: str = os.getenv("TOKEN_BOT")
ADMINS_ID: List[int] = list(map(int, (os.getenv("ADMINS_ID").split())))

PG_USER: str = os.getenv('PG_USER')
PG_PASS: str = os.getenv('PG_PASS')
DATABASE: str = os.getenv('DATABASE')
IP: str = os.getenv("IP")

PG_URL = f'postgresql://{PG_USER}:{PG_PASS}@{IP}/{DATABASE}'

TIME_MUTE = 20
DEFAULT_RATE_LIMIT = 1

TIMEZONE = pytz.timezone('Europe/Moscow')
