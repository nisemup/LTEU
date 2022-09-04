import asyncio
import logging
import uvicorn
import os

from multiprocessing import Process
from pathlib import Path
from bot import loader as load
from bot.requests import Groups
from aiogram import Bot, Dispatcher, executor, types
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent

logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    datefmt="%H:%M:%S",
    format="[%(asctime)s] %(levelname)s | %(module)s-%(funcName)s (%(lineno)d): %(message)s"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

load_dotenv(BASE_DIR / "settings" / ".env")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


class MyBot:
    dp = load.dp
    Dispatcher.set_current(load.dp)

    @classmethod
    def run(cls):
        executor.start_polling(cls.dp, on_startup=cls.on_startup, on_shutdown=cls.on_shutdown)

    @staticmethod
    async def on_startup(dp: Dispatcher):
        await load.set_commands()
        await load.register_handlers(dp)

    @staticmethod
    async def on_shutdown(dp: Dispatcher):
        await dp.storage.close()
        await dp.storage.wait_closed()


class MyServer:
    app = get_asgi_application()

    config = uvicorn.Config(app=app, loop=loop, port=8000)
    server = uvicorn.Server(config=config)

    @classmethod
    def run(cls):
        asyncio.run(cls.on_startup())
        asyncio.run(cls.server.serve())
        asyncio.run(cls.on_shutdown())

    @staticmethod
    async def on_startup() -> None:
        pass

    @staticmethod
    async def on_shutdown() -> None:
        pass


def run_app():
    bot = Process(target=MyBot.run)
    server = Process(target=MyServer.run)

    server.start()
    bot.start()


if __name__ == "__main__":
    run_app()
