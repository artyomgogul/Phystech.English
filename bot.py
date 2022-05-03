import re
import telebot
from telebot import types
bot = telebot.TeleBot('5257425523:AAHSyU-1P_-KHZXgaItpJhngoiwe1PQXzkc')


# Чекает первый раз чел пишет боту или нет и заносит его в базу 
@bot.message_handler(content_types=['text'])
def main_menu(message):
    
    with open("english.txt", "r", encoding="utf-8") as file:
        users = file.read().split(' ')[:-1]
        
    counter = 0
    
    for user in users:
        print(user)
        print(user[:user.index('-')])
        print('file:', user[:user.index('-')], 'chat: ', str(message.chat.id), 'vsego: ', users)
        if user[:user.index('-')] == str(message.chat.id):
            KB = types.InlineKeyboardMarkup(row_width=1)
            but1 = types.InlineKeyboardButton(text='Изменить уровень английского', callback_data='chng')
            but2 = types.InlineKeyboardButton(text='Потренировать грамматику', callback_data='gram') # норм назвать
            but3 = types.InlineKeyboardButton(text='Потренировать слова', callback_data='words')
            KB.add(but1, but2, but3)
            bot.send_message(message.chat.id, "<b>Чем бы вы хотели заняться?</b> ", parse_mode="HTML", reply_markup=KB)
            
            counter = 1
            break
            
    if counter == 0:
        KB = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Elementary', callback_data='elem')
        but2 = types.InlineKeyboardButton(text='Pre-Intermediate', callback_data='pre')
        but3 = types.InlineKeyboardButton(text='Intermediate', callback_data='inter')
        but4 = types.InlineKeyboardButton(text='Upper-Intermediate', callback_data='upper')
        KB.add(but1, but2, but3,but4)
        bot.send_message(message.chat.id, "(какое нибудь приветствие) <b>Выберите свой уровень английского</b> ", parse_mode="HTML", reply_markup=KB)

        
        
# Главное меню
@bot.callback_query_handler(func=lambda c: c.data)
def main_menu(callback):
    if callback.data == 'elem' or callback.data == 'pre' or callback.data == 'inter' or callback.data == 'upper':
        with open("english.txt", "a", encoding="utf-8") as file:
            file.write(str(callback.message.chat.id) + '-' + callback.data + ' ')
        KB = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Изменить уровень английского', callback_data='chng')
        but2 = types.InlineKeyboardButton(text='Потренировать грамматику', callback_data='gram') # норм назвать
        but3 = types.InlineKeyboardButton(text='Потренировать слова', callback_data='words')
        KB.add(but1, but2, but3)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="<b>Уровень выбран! Чем бы вы хотели заняться?</b> ", parse_mode="HTML", reply_markup=KB)
        
        
        
# @bot.callback_query_handler(func=lambda m: m.data)
# def main_menu_answer(callback):
    
    KB = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton(text='Elementary', callback_data='elem')
    but2 = types.InlineKeyboardButton(text='Pre-Intermediate', callback_data='pre')
    but3 = types.InlineKeyboardButton(text='Intermediate', callback_data='inter')
    but4 = types.InlineKeyboardButton(text='Upper-Intermediate', callback_data='upper')
    KB.add(but1, but2, but3,but4)

    if callback.data == 'gram':
        bot.send_message(chat_id=callback.message.chat.id, text="<b>Нет</b>", parse_mode="HTML")
        
    if callback.data == 'words':
        bot.send_message(chat_id=callback.message.chat.id, text="<b>Нет</b>", parse_mode="HTML")
        
    if callback.data == 'chng':
        new_users = []
        
        with open("english.txt", "r", encoding="utf-8") as file:
            old_users = file.read().split(' ')[:-1]
            
        for old_user in old_users:
            if old_user[:old_user.index('-')] != str(callback.message.chat.id):
                new_users.append(old_user)
                
        with open("english.txt", "w", encoding="utf-8") as file:
            file.write(" ".join(new_users) + " ")
        
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Выберите новый уровень ", parse_mode="HTML", reply_markup=KB)
        

            
bot.polling() 
