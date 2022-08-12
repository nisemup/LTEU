import keyboard as key
from language import uk_UA as t
from settings.config import c_get
from database import connect
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class TimeTable(StatesGroup):
    wait_day = State()
    cb_mon = State()


async def cmd_timetable(message: types.Message, state: FSMContext):
    db, cursor = connect()
    cursor.execute(f"""SELECT * FROM users WHERE id = {message.chat.id}""")
    await state.update_data(group=cursor.fetchone()[1])
    await message.answer(t.day_text, reply_markup=key.sdl())
    await TimeTable.cb_mon.set()


async def callback_register(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    try:
        if call.data == 'mon':
            if data['group'] == 1:
                await call.message.edit_text('Розклад для 151 групи\n\n' + c_get('G_1_mon'), reply_markup=key.sdl(call))
            elif data['group'] == 2:
                await call.message.edit_text('Розклад для 152 групи\n\n' + c_get('G_2_mon'), reply_markup=key.sdl(call))
            elif data['group'] == 3:
                await call.message.edit_text('Розклад для 153 групи\n\n' + c_get('G_3_mon'), reply_markup=key.sdl(call))
        elif call.data == 'tue':
            if data['group'] == 1:
                await call.message.edit_text('Розклад для 151 групи\n\n' + c_get('G_1_tue'), reply_markup=key.sdl(call))
            elif data['group'] == 2:
                await call.message.edit_text('Розклад для 152 групи\n\n' + c_get('G_2_tue'), reply_markup=key.sdl(call))
            elif data['group'] == 3:
                await call.message.edit_text('Розклад для 153 групи\n\n' + c_get('G_3_tue'), reply_markup=key.sdl(call))
        elif call.data == 'wed':
            if data['group'] == 1:
                await call.message.edit_text('Розклад для 151 групи\n\n' + c_get('G_1_wed'), reply_markup=key.sdl(call))
            elif data['group'] == 2:
                await call.message.edit_text('Розклад для 152 групи\n\n' + c_get('G_2_wed'), reply_markup=key.sdl(call))
            elif data['group'] == 3:
                await call.message.edit_text('Розклад для 153 групи\n\n' + c_get('G_3_wed'), reply_markup=key.sdl(call))
        elif call.data == 'thu':
            if data['group'] == 1:
                await call.message.edit_text('Розклад для 151 групи\n\n' + c_get('G_1_thu'), reply_markup=key.sdl(call))
            elif data['group'] == 2:
                await call.message.edit_text('Розклад для 152 групи\n\n' + c_get('G_2_thu'), reply_markup=key.sdl(call))
            elif data['group'] == 3:
                await call.message.edit_text('Розклад для 153 групи\n\n' + c_get('G_3_thu'), reply_markup=key.sdl(call))
        elif call.data == 'fri':
            if data['group'] == 1:
                await call.message.edit_text('Розклад для 151 групи\n\n' + c_get('G_1_fri'), reply_markup=key.sdl(call))
            elif data['group'] == 2:
                await call.message.edit_text('Розклад для 152 групи\n\n' + c_get('G_2_fri'), reply_markup=key.sdl(call))
            elif data['group'] == 3:
                await call.message.edit_text('Розклад для 153 групи\n\n' + c_get('G_3_fri'), reply_markup=key.sdl(call))
        await call.answer()
        return
    except Exception as ex:
        print(ex)
        return


def register_handlers_timetable(dp: Dispatcher):
    dp.register_message_handler(cmd_timetable, Text(equals=t.b_timetable, ignore_case=True), state="*")
    dp.register_callback_query_handler(callback_register, state=TimeTable.cb_mon)
