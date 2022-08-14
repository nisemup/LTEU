from asyncio import sleep
import aiogram
import keyboard as key
from language import uk_UA as t
from loader import bot
from database import Database
from aiogram import Dispatcher, types
from settings import config as config
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminMenu(StatesGroup):
    wait_menu = State()
    wait_news = State()
    wait_confirm = State()
    wait_group = State()
    wait_day = State()
    wait_lesson = State()
    wait_house = State()
    wait_presets = State()
    cb_housing = State()
    cb_edit = State()
    cb_pairs = State()


async def cmd_admin(message: types.Message, state: FSMContext):
    if message.chat.id in config.admins():
        await message.answer(t.a_hi, reply_markup=key.admin())
        await AdminMenu.wait_menu.set()
    else:
        await state.finish()
        return


async def menu(message: types.Message):
    if message.text == t.b_newsletter:  # Рассылка
        await message.answer(t.a_newsletter)
        await AdminMenu.wait_news.set()

    elif message.text == t.b_sdl:  # Расписание
        await message.answer(t.a_sdl, reply_markup=key.group())
        await AdminMenu.wait_group.set()

    elif message.text == t.b_presets:  # Пресеты
        await message.answer(t.b_presets, reply_markup=key.prst())
        await AdminMenu.wait_presets.set()
    else:
        await message.answer(t.error_text)
        return


# ------------------ Рассылка --------------------


async def newsletter(message: types.Message, state: FSMContext):
    await message.answer(message.text, reply_markup=key.send_news())
    await state.update_data(text=message.text)
    await AdminMenu.wait_confirm.set()


async def confirm_send(message: types.Message, state: FSMContext):
    if message.text == t.b_send_news:
        data = await state.get_data()
        with Database() as db:
            fetchall = db.select_all('users')
        users = [user[0] for user in fetchall]
        for user in users:
            try:
                print('Рассылка...')
                await bot.send_message(user, data['text'])
            except aiogram.exceptions.BotBlocked:
                continue
            await sleep(0.3)
        print('Рассылка выполнена!')
    else:
        await message.answer(t.error_text)
        return
    await message.answer(t.hi_text, reply_markup=key.main_success(message))
    await state.finish()


async def sdl_group(message: types.Message, state: FSMContext):
    if message.text == '1':
        await state.update_data(group='1')
    elif message.text == '2':
        await state.update_data(group='2')
    elif message.text == '3':
        await state.update_data(group='3')
    elif message.text == t.b_back:
        await message.answer(t.a_hi, reply_markup=key.admin())
        await AdminMenu.wait_menu.set()
        return
    else:
        await message.answer(t.error_text)
        return
    await message.answer(t.day_text, reply_markup=key.day())
    await AdminMenu.wait_day.set()


# ------------------ Расписание --------------------


async def sdl_day(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text == 'Понеділок':
        if data['group'] == '1':
            await message.answer(config.c_get('G_1_mon'), reply_markup=key.sdl_edit())
        elif data['group'] == '2':
            await message.answer(config.c_get('G_2_mon'), reply_markup=key.sdl_edit())
        elif data['group'] == '3':
            await message.answer(config.c_get('G_3_mon'), reply_markup=key.sdl_edit())
        await state.update_data(day='mon')

    elif message.text == 'Вівторок':
        if data['group'] == '1':
            await message.answer(config.c_get('G_1_tue'), reply_markup=key.sdl_edit())
        elif data['group'] == '2':
            await message.answer(config.c_get('G_2_tue'), reply_markup=key.sdl_edit())
        elif data['group'] == '3':
            await message.answer(config.c_get('G_3_tue'), reply_markup=key.sdl_edit())
        await state.update_data(day='tue')

    elif message.text == 'Середа':
        if data['group'] == '1':
            await message.answer(config.c_get('G_1_wed'), reply_markup=key.sdl_edit())
        elif data['group'] == '2':
            await message.answer(config.c_get('G_2_wed'), reply_markup=key.sdl_edit())
        elif data['group'] == '3':
            await message.answer(config.c_get('G_3_wed'), reply_markup=key.sdl_edit())
        await state.update_data(day='wed')

    elif message.text == 'Четвер':
        if data['group'] == '1':
            await message.answer(config.c_get('G_1_thu'), reply_markup=key.sdl_edit())
        elif data['group'] == '2':
            await message.answer(config.c_get('G_2_thu'), reply_markup=key.sdl_edit())
        elif data['group'] == '3':
            await message.answer(config.c_get('G_3_thu'), reply_markup=key.sdl_edit())
        await state.update_data(day='thu')

    elif message.text == "П'ятниця":
        if data['group'] == '1':
            await message.answer(config.c_get('G_1_fri'), reply_markup=key.sdl_edit())
        elif data['group'] == '2':
            await message.answer(config.c_get('G_2_fri'), reply_markup=key.sdl_edit())
        elif data['group'] == '3':
            await message.answer(config.c_get('G_3_fri'), reply_markup=key.sdl_edit())
        await state.update_data(day='fri')

    elif message.text == t.b_back:
        await message.answer(t.a_sdl, reply_markup=key.group())
        await AdminMenu.wait_group.set()
        return
    else:
        await message.answer(t.error_text)
        return

    await AdminMenu.cb_edit.set()


async def cb_edit(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    try:
        if call.data == 'edit':
            await state.update_data(type='edit')
            await call.message.edit_text(config.c_get(f'G_{data["group"]}_{data["day"]}'), reply_markup=key.sdl_pairs())
        elif call.data == 'full':
            await state.update_data(type='full')
            config.c_clear(data['group'], data['day'])
            await bot.send_message(config.c_get_key('SETTINGS', 'main_admin', 'settings'),
                                   f'Администратор №{call.message.chat.id} змінив розклад для {data["group"]} (день {data["day"]})')
            await call.message.edit_text(config.c_get(f'G_{data["group"]}_{data["day"]}'), reply_markup=key.sdl_pairs())
        elif call.data == 'close':
            await call.answer()
            await call.message.delete()
            await call.message.answer(t.day_text, reply_markup=key.day())
            await AdminMenu.wait_day.set()
            return
        await call.answer()
        await AdminMenu.cb_pairs.set()
    except Exception as ex:
        print(ex)
        return


async def cb_pairs(call: types.CallbackQuery, state: FSMContext):
    try:
        if call.data == 'p1':
            await state.update_data(pair='1')
        elif call.data == 'p2':
            await state.update_data(pair='2')
        elif call.data == 'p3':
            await state.update_data(pair='3')
        elif call.data == 'p4':
            await state.update_data(pair='4')
        elif call.data == 'p5':
            await state.update_data(pair='5')
        elif call.data == 'p6':
            await state.update_data(pair='6')
        elif call.data == 'close':
            await call.message.delete()
            await call.message.answer(t.day_text, reply_markup=key.day())
            await call.answer()
            await AdminMenu.wait_day.set()
            return
        data = await state.get_data()
        await call.answer()
        await call.message.delete()
        await call.message.answer(config.c_get_key(f'G_{data["group"]}_{data["day"]}', data['pair']),
                                  reply_markup=key.sdl_lesson())
        await AdminMenu.wait_lesson.set()
    except:
        return


async def sdl_lesson(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text == t.lesson_prog:
        await state.update_data(lesson=t.lesson_prog)
    elif message.text == t.lesson_office:
        await state.update_data(lesson=t.lesson_office)
    elif message.text == t.lesson_math:
        await state.update_data(lesson=t.lesson_math)
    elif message.text == t.lesson_disk:
        await state.update_data(lesson=t.lesson_disk)
    elif message.text == t.lesson_hist:
        await state.update_data(lesson=t.lesson_hist)
    elif message.text == t.lesson_pculture:
        await state.update_data(lesson=t.lesson_pculture)
    elif message.text == t.lesson_eng:
        await state.update_data(lesson=t.lesson_eng)
    elif message.text == t.lesson_eco:
        await state.update_data(lesson=t.lesson_eco)
    elif message.text == t.b_delete:
        config.c_set(f'G_{data["group"]}_{data["day"]}', data['pair'], config.c_get_key('FORM', f'n{data["pair"]}'))
        config.c_save('presets')
        await bot.send_message(config.c_get_key('SETTINGS', 'main_admin', 'settings'),
                               f'Администратор №{message.chat.id} змінив розклад для {data["group"]} (день {data["day"]} пара {data["pair"]})')
        await message.answer(config.c_get(f'G_{data["group"]}_{data["day"]}'), reply_markup=key.sdl_edit())
        await AdminMenu.cb_edit.set()
        return
    elif message.text == t.b_back:
        await message.answer(config.c_get(f'G_{data["group"]}_{data["day"]}'), reply_markup=key.sdl_edit())
        await AdminMenu.cb_edit.set()
        return
    else:
        await message.answer(t.error_text)
        return
    config.c_save('presets')
    await message.answer(t.a_sdl_housing, reply_markup=key.sdl_housing())
    await AdminMenu.cb_housing.set()


async def cb_housing(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'tb':
        await state.update_data(house='ТБ')
    elif call.data == 'm':
        await state.update_data(house='M')
    elif call.data == 'dis':
        if data['lesson'] == t.lesson_office:
            await state.update_data(house='Доступ до Zoom - '
                                          'https://zoom.us/j/96704000679?pwd=RXVBSEI4M3YrTHdFcERCbm5DYUNEQT09')
        elif data['lesson'] == t.lesson_eng:
            await state.update_data(house='Доступ до Zoom - -')
        elif data['lesson'] == t.lesson_eco:
            await state.update_data(house='Доступ до Zoom - '
                                          'https://us04web.zoom.us/j/73752947078?pwd=elFydWdaN3c1TWY3S3ZIcFFrUTdaQT09')
        elif data['lesson'] == t.lesson_disk:
            await state.update_data(house='Доступ до Zoom - '
                                          'https://us04web.zoom.us/j/78108733947?pwd=dFdPR0tYRitSSnNGWUxYOGp3aFBodz09')
        elif data['lesson'] == t.lesson_math:
            await state.update_data(house='Доступ до Zoom - '
                                          'https://zoom.us/j/92316193756?pwd=STFQT09DQngzbjJHOU1SS1d0RjNhdz09')
        elif data['lesson'] == t.lesson_prog:
            await state.update_data(house='Доступ до Zoom - '
                                          'https://us04web.zoom.us/j/7286059100?pwd=NXAvVTh4UHAyaS9CWE5mcmhDMWxPZz09 ')
        elif data['lesson'] == t.lesson_hist:
            await state.update_data(house='Доступ до Zoom - '
                                          'https://us04web.zoom.us/j/7286059100?pwd=NXAvVTh4UHAyaS9CWE5mcmhDMWxPZz09')
        elif data['lesson'] == t.lesson_pculture:
            await state.update_data(house='Доступ до Zoom - -')
        await call.message.delete()
        data = await state.get_data()
        form = config.c_get_key(f'FORM', data['pair']).format(lesson=data['lesson'], house=data['house'])
        config.c_set(f'G_{data["group"]}_{data["day"]}', data['pair'], form)
        config.c_gnrt_pre(data['group'], data['day'])
        config.c_save('presets')
        await bot.send_message(config.c_get_key('SETTINGS', 'main_admin', 'settings'),
                               f'Администратор №{call.message.chat.id} змінив розклад для {data["group"]} (день {data["day"]} пара {data["pair"]})')
        await call.message.answer(config.c_get(f'G_{data["group"]}_{data["day"]}'), reply_markup=key.sdl_edit())
        await AdminMenu.cb_edit.set()
        return
    elif call.data == 'none':
        await call.message.delete()
        data = await state.get_data()
        await state.update_data(house='-')
        form = config.c_get_key(f'FORM', data['pair']).format(lesson=data['lesson'], house=data['house'])
        config.c_set(f'G_{data["group"]}_{data["day"]}', data['pair'], form)
        config.c_gnrt_pre(data['group'], data['day'])
        config.c_save('presets')
        await bot.send_message(config.c_get_key('SETTINGS', 'main_admin', 'settings'),
                               f'Администратор №{call.message.chat.id} змінив розклад для {data["group"]} (день {data["day"]} пара {data["pair"]})')
        await call.message.answer(config.c_get(f'G_{data["group"]}_{data["day"]}'), reply_markup=key.sdl_edit())
        await AdminMenu.cb_edit.set()
        return
    await call.message.delete()
    await call.message.answer(t.a_sdl_num)
    await AdminMenu.wait_house.set()


async def sdl_housing(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data['house'] == 'ТБ':
        await state.update_data(house=f'ТБ-{message.text}')
    elif data['house'] == 'M':
        await state.update_data(house=f'M-{message.text}')
    data = await state.get_data()
    form = config.c_get_key(f'FORM', data['pair']).format(lesson=data['lesson'], house=data['house'])
    config.c_set(f'G_{data["group"]}_{data["day"]}', data['pair'], form)
    config.c_gnrt_pre(data['group'], data['day'])
    config.c_save('presets')
    await bot.send_message(config.c_get_key('SETTINGS', 'main_admin', 'settings'),
                           f'Администратор №{message.chat.id} змінив розклад для {data["group"]} (день {data["day"]} пара {data["pair"]})')
    await message.answer(config.c_get(f'G_{data["group"]}_{data["day"]}'), reply_markup=key.sdl_edit())
    await AdminMenu.cb_edit.set()
    return


# ------------------ Пресеты --------------------


async def presets(message: types.Message):
    if message.text == t.b_back:
        await message.answer(t.a_hi, reply_markup=key.admin())
        await AdminMenu.wait_menu.set()
        return
    elif message.text == t.b_prst_lc:
        config.c_set('SETTINGS', 'preset', 'lectures', 'settings')
        await message.answer(t.a_prst_lc, reply_markup=key.admin())
    elif message.text == t.b_prst_pr:
        config.c_set('SETTINGS', 'preset', 'practice', 'settings')
        await message.answer(t.a_prst_pr, reply_markup=key.admin())
    await AdminMenu.wait_menu.set()
    return


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cmd_admin, Text(equals=t.b_admin, ignore_case=True), state="*")
    dp.register_message_handler(menu, state=AdminMenu.wait_menu)
    dp.register_message_handler(newsletter, state=AdminMenu.wait_news)
    dp.register_message_handler(confirm_send, state=AdminMenu.wait_confirm)
    dp.register_message_handler(sdl_group, state=AdminMenu.wait_group)
    dp.register_message_handler(sdl_day, state=AdminMenu.wait_day)
    dp.register_message_handler(sdl_lesson, state=AdminMenu.wait_lesson)
    dp.register_message_handler(sdl_housing, state=AdminMenu.wait_house)
    dp.register_message_handler(presets, state=AdminMenu.wait_presets)
    dp.register_callback_query_handler(cb_housing, state=AdminMenu.cb_housing)
    dp.register_callback_query_handler(cb_edit, state=AdminMenu.cb_edit)
    dp.register_callback_query_handler(cb_pairs, state=AdminMenu.cb_pairs)
