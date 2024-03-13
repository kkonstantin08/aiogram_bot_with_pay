from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard


async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.from_user.id, f'Привет {
    # message.from_user.first_name}.Рад видеть тебя')
    await message.answer(
        f'Привет {message.from_user.first_name}.Рад видеть тебя',
        reply_markup=loc_tel_poll_keyboard)
    # await message.reply(
    #     f'Привет {message.from_user.first_name}.Рад видеть тебя')


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил локацию!\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
