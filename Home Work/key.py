from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
    row_width=2
)


s = KeyboardButton('/start')
q = KeyboardButton('/quiz')
p = KeyboardButton('/photo')
site = KeyboardButton('/site')
b = KeyboardButton('/bye')
start_markup.add(s, q, p, site,b)