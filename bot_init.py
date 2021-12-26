from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
token = '5000663222:AAFZvEvHl9EmyMVen2N52UJCqQiX3MwsaY8'
WEBHOOK_HOST = 'https://aiogram-bot-for-u.herokuapp.com'
WEBHOOK_PATH = '/webhook/' + token
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001

bot = Bot(token)
dp = Dispatcher(bot, storage=storage)
group_chat_id = '-535090506'
