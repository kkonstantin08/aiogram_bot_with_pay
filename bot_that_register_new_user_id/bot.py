import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.dispatcher.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER


API_TOKEN = '6741853928:AAHC7FVsukNoVYNzXkK1fjKKZr-7Qo_FPY8'

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
async def start():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.message.register(new_member, Command(commands=['start', 'run']))

@dp.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def new_member(message: types.Message):
    logging.info(f"new_member : {message}")
    chat_id = message.chat.id
    user_id = message.from_user.id
    await asyncio.sleep(10)
    await bot.kick_chat_member(chat_id, user_id)


if __name__ == '__main__':
    asyncio.run(start())
