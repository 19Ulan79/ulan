from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot,dp
import random
import logging

@dp.message_handler(commands=['start'])
async def returnn(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Привет, {message.from_user.full_name}!")

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    media = [ "![](../../Pictures/Camera Roll/156676658538.jpg)"
"![](../../Pictures/Camera Roll/159707550289.jpg)"
"![](../../Pictures/Camera Roll/a3cc636f9ec0c4265c56ccb6d3d6c983.jpeg)"
"![](../../Pictures/Camera Roll/165273817441.jpg)"
"![](../../Pictures/Camera Roll/1528281666.jpg)" ]
    photo = open(random.choice(media), 'rb')
    await bot.send_photo(message.chat.id,photo=photo)

@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton("Next question", callback_data="button_call")
    markup.add(button_call)
    question = "Кто самый крутой в группе?"
    answers = [
        "Денис Катрич",
        "Бигдик",
        "Эрен",
        "Али лентяй",
        "Мара укам"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        explanation='Конечно ... это же ты!',
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call")
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("Next question", callback_data="button_call1")
    markup.add(button_call1)
    question = "Как зовут новенькую девушку в группе?"
    answers = [
        "Гульчетай",
        "Маша",
        "Алия",
        "Жамиля",
        "Сайрагул"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        open_period=10,
        explanation='Извените не знал...'
    )

@dp.message_handler()
async def returnn(message: types.Message):
    try:
        k=int(message.text)
        await bot.send_message(message.from_user.id,k*k)
    except:
        await bot.send_message(message.from_user.id, message.text)
        await bot.send_message(message.chat.id, "hi")
        await message.answer("That's answer!")
        await message.reply("That's reply")
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)
