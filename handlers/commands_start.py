from aiogram import types
from misc import dp,bot
import sqlite3
from .sqlit import reg_user
from aiogram.dispatcher import FSMContext
from .sqlit import stata_user
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

photo1 = 'AgACAgIAAxkBAAMHYPrLWmxQbWH2LOV3_8DOiiSTuBEAAqiyMRso7NlL8lN_eq5QZZUBAAMCAAN5AAMgBA'  # Одноус на связи

class st_reg(StatesGroup):
    st_name = State()
    st_fname = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message,state: FSMContext):
    q = reg_user(message.chat.id)
    try:
        q = int(q)

    except:
        markup = types.InlineKeyboardMarkup()
        bat1 = types.InlineKeyboardButton(text='Пройти Тест', callback_data='start_go')
        markup.add(bat1)

        await bot.send_photo(message.chat.id,photo=photo1,caption = """<b>Одноус на связи 🤙</b>
    
Сразу к мясу, и так мы сейчас ведём набор на август, в спринт) 
    
Спринт - это наша движуха по заработку в интернете, с мобилки)
    
Для того чтобы принят участи, необходимо пройти 9 тестов!
    
Тест очень важен, он покажет сможем ли мы сделать совместный результат🚀
    
Отвечай честно, и с улыбкой ☺️""",parse_mode='html',reply_markup=markup)
