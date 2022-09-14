from aiogram import types
from .database import Database
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
    with Database() as db:
        if aid in db.get_admins():
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
    odd = types.InlineKeyboardButton(text=t.b_prst_lc, callback_data='odd')
    even = types.InlineKeyboardButton(text=t.b_prst_pr, callback_data='even')
    keyboard.add(odd, even)
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
    mon = types.InlineKeyboardButton(text='Пн', callback_data='monday')
    tue = types.InlineKeyboardButton(text='Вт', callback_data='tuesday')
    wed = types.InlineKeyboardButton(text='Ср', callback_data='wednesday')
    thu = types.InlineKeyboardButton(text='Чт', callback_data='thursday')
    fri = types.InlineKeyboardButton(text='Пт', callback_data='friday')
    sat = types.InlineKeyboardButton(text='Cб', callback_data='saturday')
    close = types.InlineKeyboardButton(text='Закрити', callback_data='close')
    if call == 'None':
        pass
    else:
        if call.data == 'monday':
            mon = types.InlineKeyboardButton(text='👁', callback_data='monday')
        elif call.data == 'tuesday':
            tue = types.InlineKeyboardButton(text='👁', callback_data='tuesday')
        elif call.data == 'wednesday':
            wed = types.InlineKeyboardButton(text='👁', callback_data='wednesday')
        elif call.data == 'thursday':
            thu = types.InlineKeyboardButton(text='👁', callback_data='thursday')
        elif call.data == 'friday':
            fri = types.InlineKeyboardButton(text='👁', callback_data='friday')
        elif call.data == 'saturday':
            sat = types.InlineKeyboardButton(text='👁', callback_data='saturday')
    keyboard.add(mon, tue, wed, thu, fri, sat)
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
