from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()
token = '5000663222:AAFZvEvHl9EmyMVen2N52UJCqQiX3MwsaY8'
WEBHOOK_HOST = 'https://aiogram-bot-for-u.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{token}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.environ.get('PORT'))

bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
group_chat_id = '-535090506'
