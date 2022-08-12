from aiogram.dispatcher import FSMContext

import keyboard as key
import text as t
from database import connect, update_db
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class Settings(StatesGroup):
    menu_chosen = State()
    wait_notification = State()
    wait_group = State()


async def menu(message: types.Message):
    await message.answer(t.b_menu_chosen, reply_markup=key.settings())
    await Settings.menu_chosen.set()


async def type_chosen(message: types.Message):
    if message.text == t.b_notification:
        await message.answer(t.b_notification, reply_markup=key.chosen_on())
        await Settings.wait_notification.set()
    elif message.text == t.b_group:
        await message.answer(t.group_text, reply_markup=key.group())
        await Settings.wait_group.set()
    else:
        await message.answer(t.error_text)
        return


async def notification(message: types.Message, state: FSMContext):
    if message.text == t.b_on_off:
        db, cursor = connect()
        cursor.execute(f"""SELECT notification FROM users WHERE id = {message.chat.id}""")
        if cursor.fetchone()[0] == 1:
            update_db(message, 'notification', 0)
            await message.answer(t.off_ntfc, reply_markup=key.main_success(message))
        else:
            update_db(message, 'notification', 1)
            await message.answer(t.on_ntfc, reply_markup=key.main_success(message))
        await state.finish()
    elif message.text == t.b_back:
        await message.answer(t.b_menu_chosen, reply_markup=key.settings())
        await Settings.menu_chosen.set()
    else:
        await message.answer(t.error_text)
        return


async def group(message: types.Message, state: FSMContext):
    if message.text == '1':
        update_db(message, 'group_id', 1)
    elif message.text == '2':
        update_db(message, 'group_id', 2)
    elif message.text == '3':
        update_db(message, 'group_id', 3)
    elif message.text == t.b_back:
        await message.answer(t.b_menu_chosen, reply_markup=key.settings())
        await Settings.menu_chosen.set()
        return
    else:
        await message.answer(t.error_text)
        return
    await message.answer(t.group_change.format(message.text), reply_markup=key.main_success(message))
    await state.finish()


def register_handlers_settings(dp: Dispatcher):
    dp.register_message_handler(menu, Text(equals=t.b_settings, ignore_case=True), state="*")
    dp.register_message_handler(type_chosen, state=Settings.menu_chosen)
    dp.register_message_handler(notification, state=Settings.wait_notification)
    dp.register_message_handler(group, state=Settings.wait_group)
