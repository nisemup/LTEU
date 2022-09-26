import asyncio
import aiogram
import sys
from datetime import datetime, timedelta
from bot.database import Database
from bot.language import uk_UA as t
from bot.loader import bot
from bot.utils import get_week_type, create_schedule, create_pre, days


async def on_startup(argv):
    date = datetime.now()
    date = datetime.weekday((date + timedelta(days=1))) if argv[1] == 'pre' else datetime.weekday(date)
    date = days[date]

    with Database() as db:
        users = db.get_uids_notif()
        for user in users:
            gid = db.get_group(user)
            data = db.get_day(gid, date, get_week_type())
            data = create_pre(data) if argv[1] == 'pre' else t.hi + create_schedule(data)[date] + t.form_footer
            try:
                await bot.send_message(user, data, disable_web_page_preview=True)
            except aiogram.utils.exceptions.BotBlocked:
                continue
            await asyncio.sleep(0.3)

    await asyncio.sleep(1)


asyncio.get_event_loop().run_until_complete(on_startup(sys.argv))
