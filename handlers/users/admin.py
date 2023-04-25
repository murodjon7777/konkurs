import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers",  )
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="reklama ---------------------------")
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
    
@dp.message_handler(text="📊 Рейтинг")
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    text=''
    i=1
    print(users)
    for user in users:
        ism=user[1]
        reyting=user[3]
        text=text+f"{i}-o'rin {ism}  •  {reyting} \n"
        i=i+1
    await message.answer(text=text)
     
    
    
