from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎁 ТАНЛОВДА ИШТИРОК ЭТИШ"),
        ],
        [
            KeyboardButton(text="🎁 Совғалар"),
            KeyboardButton(text="👤 Балларим"),
        ],
        [
            KeyboardButton(text="📊 Рейтинг"),
            KeyboardButton(text="💡 Шартлар"),
        ],
    ],
    resize_keyboard=True
)