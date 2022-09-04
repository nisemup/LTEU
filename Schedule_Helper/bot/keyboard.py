from aiogram import types
from .language import uk_UA as t


def inline_choose(data):
    keyboard = types.InlineKeyboardMarkup()
    for key in data:
        keyboard.add(types.InlineKeyboardButton(text=key, callback_data=key))
    return keyboard


def back():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard


def cancel():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_cancel)
    return keyboard


def group():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(t.b_sdl_add)
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard


def day():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(t.monday, t.tuesday, t.wednesday)
    keyboard.add(t.thursday, t.friday, t.saturday)
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard


def main_menu(aid):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_timetable)
    keyboard.add(t.b_settings)
    if aid in admins():
        keyboard.add(t.b_admin)
    return keyboard


def settings():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_notification)
    keyboard.add(t.b_group)
    keyboard.add(t.b_cancel)
    return keyboard


def chosen_on():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_on_off)
    keyboard.add(t.b_back)
    return keyboard


def admin():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_newsletter)
    keyboard.add(t.b_sdl)
    keyboard.add(t.b_presets)
    keyboard.add(t.b_cancel)
    return keyboard


def send_news():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_send_news)
    keyboard.add(t.b_cancel)
    return keyboard


def pair_type():
    keyboard = types.InlineKeyboardMarkup()
    lc = types.InlineKeyboardButton(text=t.b_prst_lc, callback_data='lc')
    pr = types.InlineKeyboardButton(text=t.b_prst_pr, callback_data='pr')
    keyboard.add(lc, pr)
    return keyboard


def pairs():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    buttons = [types.KeyboardButton(text=pair) for pair in t.pair_name]
    keyboard.add(*buttons)
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard


def sdl_confirm():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(t.b_sdl_confirm_end)
    keyboard.add(t.b_sdl_confirm_return)
    keyboard.add(t.b_cancel)
    return keyboard


def sdl(call='None'):
    keyboard = types.InlineKeyboardMarkup()
    mon = types.InlineKeyboardButton(text='Пн', callback_data='mon')
    tue = types.InlineKeyboardButton(text='Вт', callback_data='tue')
    wed = types.InlineKeyboardButton(text='Ср', callback_data='wed')
    thu = types.InlineKeyboardButton(text='Чт', callback_data='thu')
    fri = types.InlineKeyboardButton(text='Пт', callback_data='fri')
    close = types.InlineKeyboardButton(text='Закрити', callback_data='close')
    if call.data == 'mon':
        mon = types.InlineKeyboardButton(text='👁', callback_data='mon')
    elif call.data == 'tue':
        tue = types.InlineKeyboardButton(text='👁', callback_data='tue')
    elif call.data == 'wed':
        wed = types.InlineKeyboardButton(text='👁', callback_data='wed')
    elif call.data == 'thu':
        thu = types.InlineKeyboardButton(text='👁', callback_data='thu')
    elif call.data == 'fri':
        fri = types.InlineKeyboardButton(text='👁', callback_data='fri')
    keyboard.add(mon, tue, wed, thu, fri)
    keyboard.add(close)
    return keyboard


def sdl_edit():
    keyboard = types.InlineKeyboardMarkup()
    edit = types.InlineKeyboardButton(text='Редагувати', callback_data='edit')
    delete = types.InlineKeyboardButton(text='Видалити', callback_data='full')
    close = types.InlineKeyboardButton(text='Закрити', callback_data='close')
    keyboard.add(edit, delete)
    keyboard.add(close)
    return keyboard


def prst():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_prst_pr, t.b_prst_lc)
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard
