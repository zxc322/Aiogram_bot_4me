import logging
import sqlite_db
from aiogram.utils.executor import start_webhook
import admin
import client
from bot_init import dp, bot, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH, WEBHOOK_URL


async def on_startup(_):
    print('Bot started . . .')
    await bot.set_webhook(WEBHOOK_URL)
    sqlite_db.sql_start()

logging.basicConfig(level=logging.INFO)
client.register(dp)

admin.register_admin(dp)

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')



if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
