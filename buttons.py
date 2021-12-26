from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_btn = InlineKeyboardButton(text='Список товаров', callback_data='menu')
url_button = InlineKeyboardButton(text='Link', url='https://www.instagram.com')
menu_kb = InlineKeyboardMarkup(row_width=2).row(menu_btn).insert(url_button)

admin_b1 = InlineKeyboardButton(text='Загрузить', callback_data='load')
admin_b2 = InlineKeyboardButton(text='Удалить', callback_data='delete')
admin_menu = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True).row(admin_b1).insert(admin_b2)

