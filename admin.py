from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bot_init import bot
from buttons import admin_menu
from aiogram.dispatcher.filters import Text
import sqlite_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    page = State()
    link = State()
    price = State()


async def admin(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(ID, 'Привет, это сообщение могут видеть только админы групы,\n'
                               'вот все возможные команды для админа: \n'
                               'вывести чат ID : /show (сообщение прийдёт тебе в личку от бота.\n\n'
                               'Чтобы загрузить новый товар нажми "Загрузить"\n'
                               'Чтобы прервать состояние ввода введи "cancel" или выполни команду /cancel\n\n'
                               'Чтобы удалить товар из списка нажми "Удалить")',
                           reply_markup=admin_menu)
    await message.delete()


async def callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.delete(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} deleted !', show_alert=True)


async def delete(callback: types.CallbackQuery):
    if callback.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for i in read:
            await bot.send_photo(callback.from_user.id, i[0],
                                 f'Name:\n{i[1]}\n\nDescription:\n{i[2]}\n\nMore information and photos :'
                                 f' {i[3]}\n\nOrder link: {i[4]}\n\n Price: {i[-1]} $')
            await bot.send_message(callback.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {i[1]}', callback_data=f'del {i[1]}')))


async def load(callback: types.CallbackQuery):
    if callback.from_user.id == ID:
        await FSMAdmin.photo.set()
        await callback.message.answer('Import photo . . .')
        await callback.answer()
    else:
        await callback.message.answer('X Y Z')
        await callback.answer()


async def cancel(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('CANCELED')
    else:
        await message.reply('X Y Z')


async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Nice !\nNow enter name . . .')
    else:
        await message.reply('X Y Z')


async def enter_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Good !\nNow enter description . . .')
    else:
        await message.reply('X Y Z')


async def enter_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Perfect !\nNow enter page link . . .')
    else:
        await message.reply('X Y Z')


async def page_link(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['page'] = message.text
        await FSMAdmin.next()
        await message.reply('Done !\nEnter order link now . . .')
    else:
        await message.reply('X Y Z')


async def order_link(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['link'] = message.text
        await FSMAdmin.next()
        await message.reply('Got it !\n Enter price $ . .')
    else:
        await message.reply('X Y Z')


async def enter_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        try:
            async with state.proxy() as data:
                data['price'] = int(message.text)

            await sqlite_db.sql_add_command(state)
            await state.finish()
            await bot.send_message(ID, 'Download completed !')
        except:
            await message.reply('Ошибка! Вводи только цифри в этом поле.')
    else:
        await message.reply('X Y Z')


async def show_chat_id(message: types.Message):
    if message.from_user.id == ID:
        await bot.send_message(ID, message.chat.id)
        await message.delete()
    else:
        await message.answer('X Y Z')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(show_chat_id, commands='show')
    dp.register_message_handler(admin, commands='rt', is_chat_admin=True)
    dp.register_callback_query_handler(callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_callback_query_handler(delete, text='delete')
    dp.register_callback_query_handler(load, text='load', state=None)
    dp.register_message_handler(cancel, state='*', commands='cancel')
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types='photo', state=FSMAdmin.photo)
    dp.register_message_handler(enter_name, state=FSMAdmin.name)
    dp.register_message_handler(enter_description, state=FSMAdmin.description)
    dp.register_message_handler(page_link, state=FSMAdmin.page)
    dp.register_message_handler(order_link, state=FSMAdmin.link)
    dp.register_message_handler(enter_price, state=FSMAdmin.price)
