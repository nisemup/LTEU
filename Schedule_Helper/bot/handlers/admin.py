from .. import keyboard as key
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from ..utils import *


class AdminMenu(StatesGroup):
    wait_menu = State()
    wait_news = State()
    wait_confirm = State()
    sdl_menu = State()
    sdl_fac = State()
    sdl_group = State()
    sdl_type = State()
    sdl_day = State()
    sdl_number = State()
    sdl_name = State()
    sdl_start = State()
    sdl_end = State()
    sdl_classroom = State()
    sdl_register = State()
    wait_presets = State()


async def cmd_admin(message: types.Message, state: FSMContext):
    if message.chat.id in config.admins():
        await add_user(message.chat.id)
        await message.answer(t.a_hi, reply_markup=key.admin())
        await AdminMenu.wait_menu.set()
    else:
        await state.finish()
        return


async def menu(message: types.Message):
    if message.text == t.b_newsletter:  # Розсилка
        await message.answer(t.a_newsletter)
        await AdminMenu.wait_news.set()

    elif message.text == t.b_sdl:  # Розклад
        await message.answer(t.a_sdl, reply_markup=key.group())
        await AdminMenu.sdl_menu.set()

    elif message.text == t.b_presets:  # Пресети
        await message.answer(t.b_presets, reply_markup=key.prst())
        await AdminMenu.wait_presets.set()
    else:
        await message.answer(t.error_text)
        return


# ------------------ Розсилка --------------------


async def newsletter(message: types.Message, state: FSMContext):
    await message.answer(message.text, reply_markup=key.send_news())
    await state.update_data(text=message.text)
    await AdminMenu.wait_confirm.set()


# async def confirm_send(message: types.Message, state: FSMContext):
#     if message.text == t.b_send_news:
#         data = await state.get_data()
#         # with Database() as db:
#         #     fetchall = db.select_all('users')
#         users = [user[0] for user in fetchall]
#         for user in users:
#             try:
#                 print('Рассылка...')
#                 await bot.send_message(user, data['text'])
#             except aiogram.exceptions.BotBlocked:
#                 continue
#             await sleep(0.3)
#         print('Рассылка выполнена!')
#     else:
#         await message.answer(t.error_text)
#         return
#     await message.answer(t.hi_text, reply_markup=key.main_menu(message.chat.id))
#     await state.finish()


# ------------------ Розклад --------------------


async def sdl_menu(message: types.Message):
    if message.text == t.b_sdl_add:
        Profiles.objects.get_or_create(
            user_id=message.chat.id,
            group_id="ASGFGNI34123AA",
            notification=True
        )
        await message.answer(t.a_sdl_fac, reply_markup=key.inline_choose('faculty', 'groups'))
        await AdminMenu.sdl_fac.set()
    elif message.text == t.b_back:
        await message.answer(t.a_hi, reply_markup=key.admin())
        await AdminMenu.wait_menu.set()
        return
    else:
        await message.answer(t.error_text)
        return


async def sdl_fac(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(faculty=call.data)
    await call.message.edit_text(t.faculty_confirm + call.data)
    await call.message.answer(t.group_message,
                              reply_markup=key.inline_choose('group_num', 'groups', 'faculty', call.data, True))
    await call.answer()
    await AdminMenu.sdl_group.set()


async def sdl_group(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(group=call.data)
    await call.message.edit_text(t.group_confirm + call.data)
    await call.message.answer(t.a_sdl_type, reply_markup=key.pair_type())
    await call.answer()
    await AdminMenu.sdl_type.set()


async def sdl_type(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(p_type=call.data)
    await call.message.edit_text(t.type_confirm + call.data)
    await call.message.answer(t.day_text, reply_markup=key.day())
    await AdminMenu.sdl_day.set()


async def sdl_day(message: types.Message, state: FSMContext):
    if message.text in [day_translate[x] for x in day_translate]:
        await state.update_data(day=message.text)
        await message.answer(t.a_sdl_pair, reply_markup=key.pairs())
        await AdminMenu.sdl_number.set()
    elif message.text == t.b_back:
        await message.answer(t.a_sdl, reply_markup=key.group())
        await AdminMenu.sdl_menu.set()
        return
    else:
        await message.answer(t.error_text)
        return


async def sdl_number(message: types.Message, state: FSMContext):
    if message.text in t.pair_name:
        await state.update_data(number=message.text)
        await message.answer(t.a_sdl_name, reply_markup=key.back())
        await AdminMenu.sdl_name.set()
    elif message.text == t.b_back:
        await call.message.answer(t.day_text, reply_markup=key.day())
        await AdminMenu.sdl_day.set()
        return
    else:
        await message.answer(t.error_text)
        return


async def sdl_name(message: types.Message, state: FSMContext):
    if message.text == t.b_back:
        await message.answer(t.a_sdl_pair, reply_markup=key.pairs())
        await AdminMenu.sdl_number.set()
        return
    else:
        await state.update_data(name=message.text)
        await message.answer(t.a_sdl_start, reply_markup=key.back())
        await AdminMenu.sdl_start.set()


async def sdl_start(message: types.Message, state: FSMContext):
    if message.text == t.b_back:
        await message.answer(t.a_sdl_name, reply_markup=key.back())
        await AdminMenu.sdl_name.set()
        return
    else:
        await state.update_data(start=message.text)
        await message.answer(t.a_sdl_end, reply_markup=key.back())
        await AdminMenu.sdl_end.set()


async def sdl_end(message: types.Message, state: FSMContext):
    if message.text == t.b_back:
        await message.answer(t.a_sdl_start, reply_markup=key.back())
        await AdminMenu.sdl_start.set()
        return
    else:
        await state.update_data(end=message.text)
        await message.answer(t.a_sdl_housing, reply_markup=key.back())
        await AdminMenu.sdl_classroom.set()


async def sdl_classroom(message: types.Message, state: FSMContext):
    if message.text == t.b_back:
        await message.answer(t.a_sdl_end, reply_markup=key.back())
        await AdminMenu.sdl_end.set()
        return
    else:
        await state.update_data(classroom=message.text)
        data = await state.get_data()
        await message.answer(t.a_sdl_result.format(data['number'],
                                                   data['name'],
                                                   data['start'],
                                                   data['end'],
                                                   data['classroom']),
                             reply_markup=key.back())
        await AdminMenu.sdl_register.set()


async def sdl_register(message: types.Message, state: FSMContext):
    with Database as db:
        data = await state.get_data()
        if message.text == t.b_sdl_confirm_end:
            await message.edit_text(t.success)
            await state.finish()
        elif message.text == t.b_sdl_confirm_return:
            await message.answer(t.a_sdl_pair, reply_markup=key.pairs())
            await AdminMenu.sdl_number.set()
        elif message.text == t.b_back:
            await message.answer(t.a_sdl_housing, reply_markup=key.back())
            await AdminMenu.sdl_register.set()
        else:
            await message.answer(t.error_text)
        return


# ------------------ Пресети --------------------


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
    #dp.register_message_handler(confirm_send, state=AdminMenu.wait_confirm)

    dp.register_message_handler(sdl_menu, state=AdminMenu.sdl_menu)
    dp.register_callback_query_handler(sdl_fac, state=AdminMenu.sdl_fac)
    dp.register_callback_query_handler(sdl_group, state=AdminMenu.sdl_group)
    dp.register_callback_query_handler(sdl_type, state=AdminMenu.sdl_type)
    dp.register_message_handler(sdl_day, state=AdminMenu.sdl_day)
    dp.register_message_handler(sdl_number, state=AdminMenu.sdl_number)
    dp.register_message_handler(sdl_name, state=AdminMenu.sdl_name)
    dp.register_message_handler(sdl_start, state=AdminMenu.sdl_start)
    dp.register_message_handler(sdl_end, state=AdminMenu.sdl_end)
    dp.register_message_handler(sdl_classroom, state=AdminMenu.sdl_classroom)
    dp.register_message_handler(sdl_register, state=AdminMenu.sdl_register)

    dp.register_message_handler(presets, state=AdminMenu.wait_presets)
