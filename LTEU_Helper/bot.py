from loader import bot, dp
from settings.config import c_get_key
from database import Database
from aiogram.utils import executor
from aiogram.types import BotCommand
from handlers.admin import register_handlers_admin
from handlers.common import register_handlers_common
from handlers.settings import register_handlers_settings
from handlers.timetable import register_handlers_timetable


async def set_commands():
    commands = [
        BotCommand(command="/cancel", description="Отмена действий.")
    ]
    await bot.set_my_commands(commands)


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()
    await bot.close()


async def on_startup(dp):
    with Database() as db:
        db.create_db()

    await bot.send_message(c_get_key('SETTINGS', 'main_admin', 'settings'), "! Бот успешно запущен !")

    register_handlers_common(dp)
    register_handlers_settings(dp)
    register_handlers_timetable(dp)
    register_handlers_admin(dp)

    await set_commands()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
