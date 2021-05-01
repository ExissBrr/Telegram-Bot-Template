import os
from typing import List

import pyqiwi
from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT: str = os.getenv("TOKEN_BOT")
TOKEN_QIWI: str = os.getenv("TOKEN_QIWI")

ADMINS_ID: List[int] = list(map(int, (os.getenv("ADMINS_ID").split())))

QIWI_WALLET = pyqiwi.Wallet(token=TOKEN_QIWI)
