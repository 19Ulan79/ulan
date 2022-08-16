from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from domashka.config import bot
from handlers import client


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Салалекум хозяин {message.from_user.full_name}",
                           reply_markup=client.start_markup)


# @dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"ЭТО ТЕКСТ САМ РАЗБИРАЙСЯ",
                           reply_markup=client.hi_markup)


# @dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "За сколько хочешь меня купить?! АА!? "
    answers = [
        '15к сомов', "10 сомов", "Бесплатно", "Бесценно"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Размечтался Не продаюсь",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])



