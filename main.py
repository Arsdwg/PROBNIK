import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types.input_file import FSInputFile
import logging
from dotenv import load_dotenv
from os import getenv
from random import choice

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
users_uniq = set()

@dp.message(CommandStart())
async def message(message: types.Message):
    await message.reply(f'Hi! {message.from_user.first_name}, is that you?!')
    user_id = message.from_user.id
    if user_id not in users_uniq:
        users_uniq.add(user_id)
    await message.answer(f"Наш бот обслуживает {len(users_uniq)} пользователей!")

@dp.message(Command('pic'))
async def send_pic(message: types.Message):
    file = FSInputFile('image/test.jpg')
    file1 = FSInputFile('image/test1.jpg')
    lis1 = [file, file1]
    random = choice(lis1)
    await message.answer_photo(photo=random)

@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    photo1 = FSInputFile("image/test1.jpg")
    await message.answer_photo(photo=photo1)
    await message.reply(f"I found you ) You're {message.from_user.first_name} , @{message.from_user.username} ,id:{message.from_user.id}")

@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply('/myinfo - will introduce you.'
                        '\n/pic - to see nice image.')

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

