from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.types import BotCommand
from .handlers.admin import register_handlers_admin
from .handlers.common import register_handlers_common
from .handlers.settings import register_handlers_settings
from .handlers.timetable import register_handlers_timetable
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "settings" / ".env")

storage = MongoStorage(host='localhost', port=27017, db_name='aiogram_fsm')
# storage = RedisStorage2('5.188.50.9', 6379, db=5, pool_size=10, prefix='my_fsm_key')

bot = Bot(token=os.getenv('BOT_API_TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


async def set_commands():
    commands = [
        BotCommand(command="/cancel", description="Скасування будь-якої дії.")
    ]
    await bot.set_my_commands(commands)


async def register_handlers(dp):
    register_handlers_common(dp)
    register_handlers_settings(dp)
    register_handlers_timetable(dp)
    register_handlers_admin(dp)
