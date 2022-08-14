import keyboard as key
from language import uk_UA as t
from database import Database
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class StartHandler(StatesGroup):
    faculty_choose = State()
    user_register = State()


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        with Database() as db:
            fetchone = db.select_db('group_id', 'users', 'id', message.chat.id)
        if fetchone[0] != 0 and not None:
            await message.answer(t.hi_text, reply_markup=key.main_success(message.chat.id))
            await state.finish()
            return
    except TypeError:
        # TODO: make exception, rework reg check
        pass
    await message.answer(t.faculty_message, reply_markup=key.inline_choose('faculty', 'groups'))
    await StartHandler.faculty_choose.set()


async def cb_faculty(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(faculty=call.data)
    await call.message.edit_text(t.faculty_confirm + call.data)
    await call.message.answer(t.group_message,
                              reply_markup=key.inline_choose('group_num', 'groups', 'faculty', call.data, True))
    await call.answer()
    await StartHandler.user_register.set()


async def user_register(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.edit_text(t.group_confirm + call.data)
    with Database() as db:
        fetchone = db.select_db('id', 'users', 'id', call.message.chat.id)
        gid = db.select_gid(data['faculty'], call.data)
        if fetchone is None:
            db.create_user(call.message.chat.id, gid[0])
    await call.message.answer(t.hi_text, reply_markup=key.main_success(call.message.chat.id))
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Відміна!", reply_markup=key.main_success(message.chat.id))
    await state.finish()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_callback_query_handler(cb_faculty, state=StartHandler.faculty_choose)
    dp.register_callback_query_handler(user_register, state=StartHandler.user_register)
    dp.register_message_handler(cancel, Text(equals=t.b_cancel, ignore_case=False), state="*")
