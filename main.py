from aiogram import filters
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.types import ContentType, Message
from core.handlers.basic import get_start, get_hello
import asyncio
from core.settings import settings
from aiogram.filters import Command,CommandStart
from aiogram import F
from core.utils.commands import set_commands
from core.handlers.basic import get_location
from core.handlers.pay import order, pre_checkout_query, succesful_payment


# import config

async def start_bot(bot: Bot):
    await set_commands(bot)


async def start():
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(succesful_payment, F.successful_payment)
    dp.message.register(get_location, F.location)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_hello, F.text == 'Привет')
    # dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
