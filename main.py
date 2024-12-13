from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from key import start_markup



TOKEN = '7853781965:AAGmyqA8hAs1BL30BLU-tIWFiE0HmT8fxKA'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name}',reply_markup=start_markup)

@dp.message_handler(commands=['bye'])
async def start(message: types.Message):
    await message.answer('good bye!')

@dp.message_handler(commands=['site'])
async def site_command(message: types.Message):



    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('geeks', url='https://geeks.kg/')
    button1 = InlineKeyboardButton('monkeytype', url='https://monkeytype.com/')
    markup.add(button, button1)
    await bot.send_message(message.chat.id, 'vyberi knopku', reply_markup=markup)


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    photo = (
        'media/l1.jpg',
        'media/l2.jpg',
        'media/l3.jpg',

    )
    ph = open(random.choice(photo), 'rb')
    await bot.send_photo(message.chat.id, photo=ph)


@dp.message_handler(commands=['quiz'])
async def quiz_command(message: types.Message):
    markup = InlineKeyboardMarkup()
    but = InlineKeyboardButton('next', callback_data='button1')
    markup.add(but)
    question = 'Сколько лет Geeks?'
    answers = [
        '10',
        '2',
        '6',
        '21'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == 'button1')
async def quiz2(call: types.callback_query):
    question = 'old Geeks name?'
    answers = [
        'geektech',
        'google',
        'bmw'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)