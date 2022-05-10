import telebot
from translate import translate
from telebot import types

bot = telebot.TeleBot('5106587413:AAF72ed2pSaHYWuNymSudE_hHEZuxtygMWw')

def keyboard_menu(message, text):
	keyboard = types.InlineKeyboardMarkup(row_width=1)

	but1 = types.InlineKeyboardButton(text='Изменить уровень английского', callback_data='changе_level')
	but2 = types.InlineKeyboardButton(text='Потренировать грамматику', callback_data='gram')
	but3 = types.InlineKeyboardButton(text='Потренировать слова', callback_data='words')
	but4 = types.InlineKeyboardButton(text='Yandex Translate', callback_data='translate')

	keyboard.add(but1, but2, but3, but4)
	bot.send_message(chat_id = message.from_user.id, text = text, parse_mode = "HTML", reply_markup = keyboard)

def keyboard_level(message, text):
	keyboard = types.InlineKeyboardMarkup(row_width=1)

	but1 = types.InlineKeyboardButton(text='Elementary', callback_data='elem')
	but2 = types.InlineKeyboardButton(text='Pre-Intermediate', callback_data='pre')
	but3 = types.InlineKeyboardButton(text='Intermediate', callback_data='inter')
	but4 = types.InlineKeyboardButton(text='Upper-Intermediate', callback_data='upper')

	keyboard.add(but1, but2, but3, but4)
	bot.send_message(chat_id=message.from_user.id, text = text, parse_mode = "HTML", reply_markup = keyboard)

# Чекает первый раз чел пишет боту или нет и заносит его в базу
@bot.message_handler(content_types=['start'])
def start_message(message):
	users = dict()
	with open("users.txt", "r", encoding="utf-8") as file:
		for line in file:
			line = line.strip()
			users.update({line[:line.index(':')]: line[line.index(':') + 1:]})

	if str(message.chat.id) in users:
		keyboard_menu(message, "<b>Чем бы вы хотели заняться?</b> ")
	else:
		keyboard_level(message, "(какое нибудь приветствие) <b>Выберите уровень английского</b> ")


# Главное меню
@bot.callback_query_handler(func=lambda c: c.data == 'elem' or c.data == 'pre' or c.data == 'inter' or c.data == 'upper' or c.data == 'mainmenu')
def main_menu(callback):
	if callback.data != 'mainmenu':
		with open("users.txt", "a", encoding="utf-8") as file:
			file.write(str(callback.message.chat.id) + ':' + callback.data + '\n')
	keyboard_menu(callback, "<b>Чем бы вы хотели заняться?</b> ")


@bot.callback_query_handler(func=lambda c: c.data == 'changе_level')
def level_english(message):
	users = dict()
	with open("users.txt", "r", encoding="utf-8") as file:
		for line in file:
			line = line.strip()
			users.update({line[:line.index(':')]: line[line.index(':') + 1:]})

	users.pop(str(message.message.chat.id))

	with open("users.txt", "w", encoding="utf-8") as file:
		for id in users:
			file.write(id + ':' + users[id] + '\n')

	keyboard_level(message, "<b>Выберите новый уровень</b> ")


@bot.callback_query_handler(func=lambda c: c.data == 'translate')
def trans(message):
	keyboard = types.InlineKeyboardMarkup(row_width=1)
	but = types.InlineKeyboardButton(text='Главное меню', callback_data='mainmenu')
	keyboard.add(but)

	bot.send_message(chat_id = message.from_user.id, text = 'Введите текст', parse_mode = "HTML", reply_markup = keyboard)


@bot.message_handler(func=lambda c: True)
def read_message(message):
	if message.text == '/start':
		start_message(message)
	else:
		transl = translate(message.text, 'ru')

		keyboard = types.InlineKeyboardMarkup(row_width=1)
		but = types.InlineKeyboardButton(text='Главное меню', callback_data='mainmenu')
		keyboard.add(but)

		bot.send_message(chat_id=message.from_user.id, text=transl, parse_mode="HTML", reply_markup=keyboard)


bot.polling()