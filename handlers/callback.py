from aiogram import types
from misc import dp, bot
import sqlite3
from aiogram.dispatcher import FSMContext
from .sqlit import update_user
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

photo2 = 'AgACAgIAAxkBAANEYPrbmQqCaTV5U4zezpbFLCRbsKgAAhSzMRso7NlLBXmAjohTHdUBAAMCAANtAAMgBA' #Прошел опрос
photo3 = 'AgACAgIAAxkBAANZYPrmQ1ibsLh3e-TBzbf-s69tPTYAAkq0MRvUvNFL60VHqyrxns0BAAMCAANzAAMgBA' # Продажное фото

video1 = 'BAACAgIAAxkBAANFYPrhGR5td7P7pVBs9VIpTbjYJ1sAAtsMAAIo7NlL22beHrkECQggBA' #в руке лист бумаги
video2 = 'BAACAgIAAxkBAANPYPrkgGNZBYxyFJK7pc-ABXhu9UMAAvQPAALUvNFLmO-QApQ5_QYgBA' # Конечное видео


time1 = 75 # Видео длится 80 секунд
time2 = 170 # Видео длится 172 секунды

class regs(StatesGroup):
    names = State()
    fnames = State()
    url_step = State()
    get_kod = State()

@dp.callback_query_handler(text='start_go')
async def start_go1(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next1')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next1')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next1')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next1')

    markup.row(bat_k,bat_a,bat_i,bat_f)
    await bot.send_message(chat_id=call.message.chat.id,text="""<b>1) Сколько тебе лет?</b>

К) до 14

А) с 14 до 17

Й) с 17 до 20

Ф) с 20 до 101""",parse_mode='html',reply_markup=markup)


@dp.callback_query_handler(text='next1')
async def start_2(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id,chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next2')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next2')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next2')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next2')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>2) С какой страны будешь?</b>

К) Россия 

А) Кыргызстан 

Й) Узбекистан 

Ф) Другая страна""", parse_mode='html', reply_markup=markup)




@dp.callback_query_handler(text='next2')
async def start_3(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next3')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next3')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next3')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next3')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>3) Сколько часов можешь уделять работе в интернете?</b>

К) 1 - 2 часа 

А) 2 - 4 часа 

Й) 4 - 6 часов 

Ф) 6 - 8 часов""", parse_mode='html', reply_markup=markup)


@dp.callback_query_handler(text='next3')
async def start_3(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next4')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next4')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next4')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next4')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>4) Сколько денег зарабатываешь в месяц, на данный момент?</b>

К) до 100$

А) от 100$ до 500$

Й) от 500$ до 1000$

Ф) от 1000$ до 🍋""", parse_mode='html', reply_markup=markup)


@dp.callback_query_handler(text='next4')
async def start_3(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next5')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next5')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next5')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next5')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>5) Знаешь ли что такое «Арбитраж трафика»?</b>

К) нет

А) да

Й) приблизительно 

Ф) я мастер Арбитража""", parse_mode='html', reply_markup=markup)


@dp.callback_query_handler(text='next5')
async def start_3(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next6')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next6')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next6')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next6')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>6) Есть ли у тебя телеграмм канал?</b>

К) нет

А) да

Й) где-то пылиться 

Ф) я активно развиваю тг""", parse_mode='html', reply_markup=markup)


@dp.callback_query_handler(text='next6')
async def start_3(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next7')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next7')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next7')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next7')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>7) Сколько роликов снимаешь в тик ток?</b>

К) много

А) не снимаю

Й) бывает иногда

Ф) я тик токер""", parse_mode='html', reply_markup=markup)

@dp.callback_query_handler(text='next7')
async def start_3(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='next8')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='next8')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='next8')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='next8')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>8) Есть ли опыт в интернет заработке?</b>

К) нет

А) немного

Й) да есть

Ф) я эксперт""", parse_mode='html', reply_markup=markup)


@dp.callback_query_handler(text='next8')
async def start_3(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)
    markup = types.InlineKeyboardMarkup()

    bat_k = types.InlineKeyboardButton(text='К', callback_data='step1')
    bat_a = types.InlineKeyboardButton(text='А', callback_data='step2')
    bat_i = types.InlineKeyboardButton(text='Й', callback_data='step2')
    bat_f = types.InlineKeyboardButton(text='Ф', callback_data='step2')

    markup.row(bat_k, bat_a, bat_i, bat_f)
    await bot.send_message(chat_id=call.message.chat.id, text="""<b>9) Был(а) на нашем Квесте по арбитражному старту?</b>

К) да

А) нет

Й) что-то слышал(а) ты делал 

Ф) не успел(а) попасть""", parse_mode='html', reply_markup=markup)


# Человек не подходит
@dp.callback_query_handler(text='step1')
async def step1_k(call: types.callback_query,state: FSMContext):
    await bot.delete_message(message_id=call.message.message_id, chat_id=call.message.chat.id)

    markup = types.InlineKeyboardMarkup()
    bat = types.InlineKeyboardButton(text='Подарок', callback_data='get_priz')
    markup.add(bat)

    await bot.send_message(chat_id=call.message.chat.id,text="""Сорри(( но тест показал, что наш короткий запуск спринта, тебе не подходит, но скоро мы запустим спринт полноценно, жди анонсы в сторис 🤗

А пока что у меня для тебя небольшой подарок 🎁""",reply_markup=markup)


@dp.callback_query_handler(text='get_priz')
async def get_priz(call: types.callback_query,state: FSMContext):
    await bot.send_message(call.message.chat.id,text="""https://telegra.ph/Arbitrazh-trafika-dlya-novichkov-pribyl-ot-50000-v-mesyac--podbor-topovyh-offerov--bez-vlozhenij-v-trafik-07-04""")


# Человек подходит
@dp.callback_query_handler(text='step2')
async def step2_k(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat = types.InlineKeyboardButton(text='Я тут 👋', callback_data='step3')
    markup.add(bat)
    await bot.send_photo(chat_id=call.message.chat.id,photo=photo2,caption="""Красава 💪

Тест пройден ✅

Лан) погнал дальше тебе рассказывать, только на кнопку жамкни 😅""",reply_markup=markup)



@dp.callback_query_handler(text='step3')
async def step3(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat = types.InlineKeyboardButton(text='Далее', callback_data='time')
    markup.add(bat)

    v = await bot.send_video(chat_id=call.message.chat.id,video=video1,reply_markup=markup)

    await asyncio.sleep(time1)

    markup2 = types.InlineKeyboardMarkup()
    bat2 = types.InlineKeyboardButton(text='Далее', callback_data='step4')
    markup2.add(bat2)

    await bot.edit_message_reply_markup(chat_id=v.chat.id,message_id=v.message_id,reply_markup=markup2)


@dp.callback_query_handler(text='time')
async def time(call: types.callback_query,state: FSMContext):
    await bot.send_message(chat_id=call.message.chat.id,text='Не торопись 😀\n'
                                                             'Сначала досмотри видео')

@dp.callback_query_handler(text='step4')
async def step4(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat = types.InlineKeyboardButton(text='Далее', callback_data='time')
    markup.add(bat)

    v = await bot.send_video(chat_id=call.message.chat.id, video=video2, reply_markup=markup)

    await asyncio.sleep(time2)

    markup2 = types.InlineKeyboardMarkup()
    bat2 = types.InlineKeyboardButton(text='Далее', callback_data='step5')
    markup2.add(bat2)

    await bot.edit_message_reply_markup(chat_id=v.chat.id, message_id=v.message_id, reply_markup=markup2)


@dp.callback_query_handler(text='step5')
async def step5(call: types.callback_query,state: FSMContext):
    await bot.send_photo(chat_id=call.message.chat.id, caption="""
    Кстати все наши ученики)  инвестировали в спринт 5$ и сделали Х100 💪 жирная окупаемость.

Как попасть в спринт?

Так как это пред запуск спринта, сделаю минимальную стоимость, чтобы каждый смог вкусить, этот кайф 😇

Стоимость - 4$ 

Для Рф - 294₽
Для Кр - 337 сом
Для Узб - 42.400 сум 
Для Кз - 1700 тенге 
Для Ук - 108 гривна 
Для Белоруссии - 10

Если курс поменялся, не проблема поменяем 👌 

Для покупки пиши мне в личку @nikolanext

После успешной оплаты, добавлю в чат ожидания)

Мест осталось (45)""",photo=photo3)
    update_user(call.message.chat.id)

