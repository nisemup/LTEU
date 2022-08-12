import keyboard as key
import text as t
from database import connect
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class StartHandler(StatesGroup):
    start_chosen = State()
    group_chosen = State()


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    db, cursor = connect()
    try:
        cursor.execute(f"""SELECT group_id FROM users WHERE id = {message.chat.id}""")
        if cursor.fetchone()[0] != 0 and not None:
            await message.answer(t.hi_text, reply_markup=key.main_success(message))
            await state.finish()
            return
    except TypeError:
        pass
    await message.answer(t.start_message, reply_markup=key.main())
    await StartHandler.start_chosen.set()


async def start_chosen(message: types.Message):
    if message.text == t.b_group:
        await message.answer(t.group_text, reply_markup=key.group())
        await StartHandler.group_chosen.set()
    else:
        await message.answer(t.error_text)
        return


async def group_chosen(message: types.Message, state: FSMContext):
    db, cursor = connect()
    cursor.execute(f"""SELECT id FROM users WHERE id = {message.chat.id}""")
    if cursor.fetchone() is None:
        cursor.execute("""INSERT INTO users VALUES (?, ?, ?)""", (message.chat.id, 0, 1))
    if message.text == '1':
        cursor.execute(f"""UPDATE users SET group_id = 1 WHERE id ={message.chat.id}""")
    elif message.text == '2':
        cursor.execute(f"""UPDATE users SET group_id = 2 WHERE id ={message.chat.id}""")
    elif message.text == '3':
        cursor.execute(f"""UPDATE users SET group_id = 3 WHERE id ={message.chat.id}""")
    elif message.text == t.b_back:
        db.commit()
        await message.answer(t.start_message, reply_markup=key.main())
        await StartHandler.start_chosen.set()
    else:
        await message.answer(t.error_text)
        return
    db.commit()
    await message.answer(t.hi_text, reply_markup=key.main_success(message))
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Відміна!", reply_markup=key.main_success(message))
    await state.finish()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(start_chosen, state=StartHandler.start_chosen)
    dp.register_message_handler(group_chosen, state=StartHandler.group_chosen)
    dp.register_message_handler(cancel, Text(equals=t.b_cancel, ignore_case=False), state="*")
