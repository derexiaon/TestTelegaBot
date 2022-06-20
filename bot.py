"""
This is a echo bot.
It echoes any incoming text messages.
"""
import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import weather


API_TOKEN = os.environ['BOT_TOKEN_HERE']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ваш ID", "Погода в Казани"]
    keyboard.add(*buttons)
    await message.reply(f"Привет {message.from_user.username}, напиши свой город, чтобы узнать погоду", reply_markup=keyboard)


@dp.message_handler(Text(equals="Ваш ID"))
async def user_id(message: types.Message):
    await message.reply(f"Ваш ID: {message.from_user.id}")


@dp.message_handler(Text(equals="Погода в Казани"))
async def weather_k(message: types.Message):
    await message.answer(weather.get_weather("Kazan"))


@dp.message_handler()
async def weather_an(message: types.Message):
    await message.answer(weather.get_weather(message.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
