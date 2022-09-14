from aiogram.dispatcher import FSMContext
from .. import keyboard as key
from ..language import uk_UA as t
from ..database import Database
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class Settings(StatesGroup):
    menu_chosen = State()
    wait_notification = State()
    wait_group = State()
    group_update = State()


async def menu(message: types.Message):
    await message.answer(t.b_menu_chosen, reply_markup=key.settings())
    await Settings.menu_chosen.set()


async def type_chosen(message: types.Message):
    if message.text == t.b_notification:
        await message.answer(t.b_notification, reply_markup=key.chosen_on())
        await Settings.wait_notification.set()
    elif message.text == t.b_group:
        username = message.from_user.username if message.from_user.username else None
        await state.update_data(username=username)
        with Database() as db:
            data = db.get_faculty()
        await message.answer(t.faculty_message, reply_markup=key.inline_choose(data))
        await Settings.wait_group.set()
    else:
        await message.answer(t.error_text)
        return


async def notification(message: types.Message, state: FSMContext):
    if message.text == t.b_on_off:
        with Database() as db:
            data = db.get_notification(message.chat.id)
            db.update_notification(message.chat.id, data)
            if data:
                await message.answer(t.off_ntfc, reply_markup=key.main_menu(message.chat.id))
            elif not data:
                await message.answer(t.on_ntfc, reply_markup=key.main_menu(message.chat.id))
            else:
                await message.answer(t.error_func, reply_markup=key.main_menu(message.chat.id))
        await state.finish()
    elif message.text == t.b_back:
        await message.answer(t.b_menu_chosen, reply_markup=key.settings())
        await Settings.menu_chosen.set()
    else:
        await message.answer(t.error_text)
        return


async def group(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(faculty=call.data)
    with Database() as db:
        data = db.get_gnum(call.data)
    await call.message.edit_text(t.faculty_confirm + call.data)
    await call.message.answer(t.group_message,
                              reply_markup=key.inline_choose(data))
    await call.answer()
    await Settings.group_update.set()


async def group_update(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.edit_text(t.group_confirm + call.data)
    with Database() as db:
        gid = db.get_gid(data['faculty'], call.data)
        if db.create_user(call.message.chat.id, gid, data['username']):
            await call.message.answer(t.hi_text, reply_markup=key.main_menu(call.message.chat.id))
            await state.finish()


def register_handlers_settings(dp: Dispatcher):
    dp.register_message_handler(menu, Text(equals=t.b_settings, ignore_case=True), state="*")
    dp.register_message_handler(type_chosen, state=Settings.menu_chosen)
    dp.register_message_handler(notification, state=Settings.wait_notification)
    dp.register_callback_query_handler(group, state=Settings.wait_group)
    dp.register_callback_query_handler(group_update, state=Settings.group_update)
