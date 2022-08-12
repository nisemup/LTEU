from aiogram import types
import text as t
from config import admins


def main():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_group)
    return keyboard


def group():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('1', '2', '3')
    keyboard.add(t.b_back)
    return keyboard


def day():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Понеділок', 'Вівторок', 'Середа')
    keyboard.add('Четвер', "П'ятниця")
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard


def lang():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_group)
    keyboard.add(t.b_back)
    return keyboard


def main_success(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_timetable)
    keyboard.add(t.b_settings)
    if message.chat.id in admins():
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


def pairs():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Первая пара', 'Вторая пара', 'Третья пара')
    keyboard.add('Четвёртая пара', 'Пятая пара', 'Шоста пара')
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard


def sdl(call='None'):
    keyboard = types.InlineKeyboardMarkup()
    mon = types.InlineKeyboardButton(text='Пн', callback_data='mon')
    tue = types.InlineKeyboardButton(text='Вт', callback_data='tue')
    wed = types.InlineKeyboardButton(text='Ср', callback_data='wed')
    thu = types.InlineKeyboardButton(text='Чт', callback_data='thu')
    fri = types.InlineKeyboardButton(text='Пт', callback_data='fri')
    if call == 'None':
        pass
    else:
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
    return keyboard


def sdl_edit():
    keyboard = types.InlineKeyboardMarkup()
    edit = types.InlineKeyboardButton(text='Редагувати', callback_data='edit')
    delete = types.InlineKeyboardButton(text='Видалити', callback_data='full')
    close = types.InlineKeyboardButton(text='Закрити', callback_data='close')
    keyboard.add(edit, delete)
    keyboard.add(close)
    return keyboard


def sdl_pairs():
    keyboard = types.InlineKeyboardMarkup()
    pair1 = types.InlineKeyboardButton(text='1', callback_data='p1')
    pair2 = types.InlineKeyboardButton(text='2', callback_data='p2')
    pair3 = types.InlineKeyboardButton(text='3', callback_data='p3')
    pair4 = types.InlineKeyboardButton(text='4', callback_data='p4')
    pair5 = types.InlineKeyboardButton(text='5', callback_data='p5')
    pair6 = types.InlineKeyboardButton(text='6', callback_data='p6')
    close = types.InlineKeyboardButton(text='Закрити', callback_data='close')
    keyboard.add(pair1, pair2, pair3)
    keyboard.add(pair4, pair5, pair6)
    keyboard.add(close)
    return keyboard


def sdl_lesson():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(t.b_delete)
    keyboard.add(t.lesson_prog, t.lesson_office)
    keyboard.add(t.lesson_math, t.lesson_disk)
    keyboard.add(t.lesson_hist, t.lesson_pculture)
    keyboard.add(t.lesson_eng, t.lesson_eco)
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard


def sdl_housing():
    keyboard = types.InlineKeyboardMarkup()
    tb = types.InlineKeyboardButton(text='ТБ', callback_data='tb')
    dis = types.InlineKeyboardButton(text='M', callback_data='m')
    m = types.InlineKeyboardButton(text='Дистанционка (ссылка)', callback_data='dis')
    none = types.InlineKeyboardButton(text='-', callback_data='none')
    keyboard.add(tb, m, none, dis)
    return keyboard


def prst():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(t.b_prst_pr, t.b_prst_lc)
    keyboard.add(t.b_back, t.b_cancel)
    return keyboard
