import sqlite3 as sq
from bot_init import bot


def sql_start():
    global base, cur
    base = sq.connect('zxc_data.db')
    cur = base.cursor()
    if base:
        print('connected !')
    base.execute('CREATE TABLE IF NOT EXISTS список_товаров(фото TEXT, название TEXT PRIMARY KEY, описание TEXT, стриничка TEXT, ссылка TEXT, цена TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO список_товаров VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(callback):
    for i in cur.execute('SELECT * FROM список_товаров').fetchall():
        await bot.send_photo(callback.from_user.id, i[0], f'Name:\n{i[1]}\n\nDescription:\n{i[2]}\n\nMore information and photos :'
                                                          f' {i[3]}\n\nOrder link: {i[4]}\n\n Price: {i[-1]} $')


async def sql_read2():
    return cur.execute('SELECT * FROM список_товаров').fetchall()


async def delete(data):
    cur.execute('DELETE FROM список_товаров WHERE название == ?', (data, ))
    base.commit()
