import asyncio
import datetime
from asyncio import sleep
import aiogram
from database import connect
import text as t
import config as c
from loader import bot


time = datetime.datetime.strftime(datetime.datetime.now(), "%a %H:%M")


async def on_startup():
    db, cursor = connect()
    print(time)
    if time == 'Sun 18:30':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('1', 'mon')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('2', 'mon')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('3', 'mon')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Mon 07:00':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_1_mon'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_2_mon'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_3_mon'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Mon 18:30':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('1', 'tue')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('2', 'tue')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('3', 'tue')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Tue 07:00':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_1_tue'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_2_tue'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_3_tue'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Tue 18:30':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('1', 'wed')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('2', 'wed')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('3', 'wed')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Wed 07:00':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_1_wed'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_2_wed'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_3_wed'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Wed 18:30':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('1', 'thu')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('2', 'thu')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('3', 'thu')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Thu 07:00':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_1_thu'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_2_thu'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_3_thu'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Thu 18:30':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('1', 'fri')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('2', 'fri')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                n, s, e, h, ct = c.get_pre('3', 'fri')
                await bot.send_message(user, t.hi_pre + t.pre.format(n, h, s, e, ct))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    elif time == 'Fri 07:00':
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 1""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_1_fri'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 2""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_2_fri'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
        cursor.execute(f"""SELECT * FROM users WHERE notification = 1 AND group_id = 3""")
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            try:
                await bot.send_message(user, t.hi + c.c_get('G_3_fri'))
            except aiogram.exceptions.BotBlocked:
                pass
            await sleep(0.3)
    await bot.send_message(c.c_get_key('SETTINGS', 'main_admin', 'settings')[0], 'Рассылка выполнена')
    await bot.close()
    await sleep(1)


asyncio.run(on_startup())
