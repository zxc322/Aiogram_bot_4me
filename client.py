from aiogram import types, Dispatcher
from buttons import menu_kb
import sqlite_db

text = 'Работа исключительно на 1000 рублей, поэтому не предлагайте больше!!!' \
       ' Мне нужно составить рекламный видеоролик об аккаунте в инстаграме,' \
       ' который пойдет в таргетированную рекламу инстаграм. ' \
       'Пост нужно сделать об аккаунте платных объявлений определенного города.\n\n' \
       'Если Вы админ введите команду /rt в груповом чате для дополнительной информации!'


async def start(message: types.Message):
    await message.answer(text, reply_markup=menu_kb)


async def menu(callback: types.CallbackQuery):
    await sqlite_db.sql_read(callback)
    #await callback.message.answer(callback.from_user.id)
    await callback.answer()


def register(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_callback_query_handler(menu, text='menu')
