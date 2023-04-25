import sqlite3
from keyboards.default.menu import menu
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    args = message.get_args()
    id=message.from_user.id 
    text=f"5balga ega boldingz" 
    # text1="Foydalanuvchi telegram botda oldindan ma" 
    name = message.from_user.full_name

    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name,ball=0)
        if args=='':
            await message.answer(f"Salom, {message.from_user.full_name}!")
        elif int(args)==id:
            await message.answer(f"Salom, {message.from_user.full_name}!")
        else: 
            user = db.get_users(args)
            print("/////////////////////////////////////////////////////")
            ball=int(user[0][3])
            ball=ball+5
            
            print(user[0][3]) 
            print("/////////////////////////////////////////////////////")
            db.update_user_ball(ball=ball,id=args) 
            await bot.send_message(chat_id=args, text=text)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
        # await bot.send_message(chat_id=args, text=text)

    await message.answer("Xush kelibsiz!",reply_markup=menu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    
@dp.message_handler(text="👤 Балларим")
async def bot_start(message: types.Message):
        id=message.from_user.id
        ball=db.get_users(id)[0][3]
        await message.answer(text=f"Toplagan balingiz {ball}")