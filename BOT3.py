import telebot
from translate import translate
from telebot import types
from random import choice
from takewords import WORDS

bot = telebot.TeleBot('5106587413:AAF72ed2pSaHYWuNymSudE_hHEZuxtygMWw')

USERS = dict()

# Клава с функциями
def keyboard_menu(message, text):
	keyboard = types.InlineKeyboardMarkup(row_width=1)

	but1 = types.InlineKeyboardButton(text='Изменить уровень английского', callback_data='changе_level')
	but2 = types.InlineKeyboardButton(text='Потренировать грамматику', callback_data='gram')
	but3 = types.InlineKeyboardButton(text='Потренировать слова', callback_data='training_words')
	but4 = types.InlineKeyboardButton(text='Yandex Translate', callback_data='translate')

	keyboard.add(but1, but2, but3, but4)
	bot.send_message(chat_id = message.from_user.id, text = text, parse_mode = "HTML", reply_markup = keyboard)


# Клава с выбором уровня
def keyboard_level(message, text):
	keyboard = types.InlineKeyboardMarkup(row_width=1)

	but1 = types.InlineKeyboardButton(text='Elementary', callback_data='eleme')
	but2 = types.InlineKeyboardButton(text='Pre-Intermediate', callback_data='prein')
	but3 = types.InlineKeyboardButton(text='Intermediate', callback_data='inter')
	but4 = types.InlineKeyboardButton(text='Upper-Intermediate', callback_data='upper')

	keyboard.add(but1, but2, but3, but4)
	bot.send_message(chat_id=message.from_user.id, text = text, parse_mode = "HTML", reply_markup = keyboard)


# Старт, выкидывает клаву с выбором уроня или гланое меню
@bot.message_handler(content_types=['start'])
def start_message(message):

	if str(message.chat.id) in USERS:
		keyboard_menu(message, "<b>Чем бы вы хотели заняться?</b> ")
	else:
		keyboard_level(message, "(какое нибудь приветствие) <b>Выберите уровень английского</b> ")


# Ловит выбор уровня, или нажатие на клавишу "главное меню"
# Выкидывает клаву с главным меню и создаёт пользователя
@bot.callback_query_handler(func=lambda c: c.data in ['eleme', 'prein', 'inter', 'upper', 'mainmenu'])
def main_menu(callback):

	if callback.data != 'mainmenu':
		USERS.update( { str(callback.message.chat.id): {'level': callback.data, 'mod': 'None'} } )

	keyboard_menu(callback, "<b>Чем бы вы хотели заняться?</b> ")


# Ловит нажатие на кнопку "изменить уровень"
# выкидывает клаву с уровнями и удаляет пользователя
@bot.callback_query_handler(func=lambda c: c.data == 'changе_level')
def level_english(message):
	USERS.pop(str(message.message.chat.id))

	keyboard_level(message, "<b>Выберите новый уровень</b> ")



@bot.callback_query_handler(func=lambda c: c.data == 'training_words')
def tr_w(callback):
	keyboard = types.InlineKeyboardMarkup(row_width=1)
	but1 = types.InlineKeyboardButton(text='С Англ на Русс', callback_data='trainingWords_en-ru')
	but2 = types.InlineKeyboardButton(text='С Русс на Англ', callback_data='trainingWords_ru-en')
	but3 = types.InlineKeyboardButton(text='Рандомно', callback_data='trainingWords_rndom')
	but4 = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
	keyboard.add(but1, but2, but3, but4)

	bot.send_message(chat_id=callback.message.chat.id, text="Выберете режим", parse_mode="HTML", reply_markup=keyboard)



@bot.callback_query_handler(func=lambda c: c.data == 'translate')
def trans(message):
	USERS[str(message.message.chat.id)]['mod'] = 'translate'

	bot.send_message(chat_id=message.from_user.id, text='Вы вводите текст, я вам перевод, для выхода в меню /menu',
	                 parse_mode="HTML")


@bot.callback_query_handler(func=lambda c: c.data in ['trainingWords_en-ru','trainingWords_ru-en','trainingWords_rndom'])
def tr(callback):
	USERS[str(callback.message.chat.id)]['mod'] = '%%%'+USERS[str(callback.message.chat.id)]['level'] + callback.data[13:]
	bot.send_message(chat_id=callback.message.chat.id,
					 text='Я пишу вам слово, вы мне его перевод, и я вас проверяю, если ответ верный, '
					      'я просто пришлю следующее слово, для выхода напишите /menu',
	                 parse_mode="HTML")

	bot.send_message(chat_id=callback.message.chat.id,
	                 text='Начнём',
	                 parse_mode="HTML")
	w1,w2 = choice(list(WORDS[USERS[str(callback.message.chat.id)]['mod'][3:14]].items()))
	USERS[str(callback.message.chat.id)]['mod'] = USERS[str(callback.message.chat.id)]['mod'] + w2
	bot.send_message(chat_id=callback.message.chat.id,
	                 text=w1,
	                 parse_mode="HTML")


# Ловит и обрабатывает все текстовые сообщения от пользователя
@bot.message_handler(func=lambda c: True)
def read_message(message):
	mod = 'None'
	if str(message.chat.id) in USERS:
		mod = USERS[str(message.chat.id)]['mod']

	if message.text == '/start':
		start_message(message)

	if message.text == '/menu':
		keyboard_menu(message, "<b>Чем бы вы хотели заняться?</b> ")

	elif mod == 'translate':   # Если пользователь будучи в режиме перевода отправляет сообщение, бот отправляет перевод

		transl = translate(message.text, 'ru')

		bot.send_message(chat_id=message.from_user.id, text=transl, parse_mode="HTML")

	elif mod[:3] == '%%%':          # Если пользователь будучи в режиме тренировки слов отправляет сообщение
		print(USERS)
		if USERS[str(message.chat.id)]['mod'][14:] == message.text:
			USERS[str(message.from_user.id)]['mod'] = USERS[str(message.from_user.id)]['mod'][:14]
			w1, w2 = choice(list(WORDS[USERS[str(message.from_user.id)]['mod'][3:]].items()))
			USERS[str(message.from_user.id)]['mod'] = USERS[str(message.from_user.id)]['mod'] + w2
			bot.send_message(chat_id=message.from_user.id,
			                 text=w1,
			                 parse_mode="HTML")

bot.polling()