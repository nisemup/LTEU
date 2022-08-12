import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from config import c_get_key, c_create


storage = MongoStorage(host='localhost', port=27017, db_name='users_fsm')
c_create()
bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
