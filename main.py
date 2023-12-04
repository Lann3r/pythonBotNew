from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from сore.Handlers.basic import get_start
import asyncio
import logging
from сore.settings import settings
from сore.Handlers.basic import callback_series

from сore.Utils.commands import set_commands
from сore.Middlewares.check_sub import CheckSubscription


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот выключен!")


async def start():
    logging.basicConfig(level=logging.INFO)

    # Объект бота
    bot = Bot(token=settings.bots.bot_token)
    # Диспетчер
    dp = Dispatcher()
    dp.callback_query.middleware(CheckSubscription())
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start']))
    dp.callback_query.register(callback_series)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print("Exiting...")
