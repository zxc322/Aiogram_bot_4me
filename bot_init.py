from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

WEBHOOK_HOST = 'https://5133-93-75-106-174.ngrok.io'
WEBHOOK_URL = f"{WEBHOOK_HOST}"
WEBHOOK_PATH = ''
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 5000
token = '5000663222:AAFZvEvHl9EmyMVen2N52UJCqQiX3MwsaY8'
bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
group_chat_id = '-535090506'