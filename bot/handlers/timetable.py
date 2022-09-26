from .. import keyboard as key
from ..language import uk_UA as t
from ..database import Database
from ..utils import create_schedule, get_week_type
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class TimeTable(StatesGroup):
    wait_day = State()
    callback_register = State()


async def cmd_timetable(message: types.Message, state: FSMContext):
    with Database() as db:
        week = get_week_type()
        gid = db.get_group(message.chat.id)
        data = db.get_schedule(gid, week)
    await state.update_data(data=create_schedule(data))
    await message.answer(t.day_text, reply_markup=key.sdl())
    await TimeTable.callback_register.set()


async def callback_register(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'close':
        await call.message.delete()
        await state.finish()
    else:
        await call.message.edit_text(
            data[call.data] + t.form_footer if data.get(call.data) is not None else t.none_text,
            reply_markup=key.sdl(call),
            disable_web_page_preview=True
        )
    await call.answer()
    return


def register_handlers_timetable(dp: Dispatcher):
    dp.register_message_handler(cmd_timetable, Text(equals=t.b_timetable, ignore_case=True), state="*")
    dp.register_callback_query_handler(callback_register, state=TimeTable.callback_register)
