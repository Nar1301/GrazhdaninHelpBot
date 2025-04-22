from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN
from templates import get_template

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Кнопки меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("Генерация шаблона документа"))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Привет! Я GrazhdaninHelpBot. Чем могу помочь?", reply_markup=menu)

@dp.message_handler(lambda message: message.text == "Генерация шаблона документа")
async def generate_document(message: types.Message):
    template = get_template("жалоба")
    await message.answer(f"Вот пример шаблона:\n\n{template}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
