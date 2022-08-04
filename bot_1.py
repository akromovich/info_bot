import telebot
import config
from telebot import types

tb = telebot.TeleBot('5555513489:AAEYI3E1rpoTDKEEpzH8N-nAgw4LYSA-dBo')

#
# @tb.message_handler()
# def user_messages(message):
#     if message.text.lower() ==  "javoh" or message.text.lower()=='жавох':
#         photo = open('static/javoh.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo)
#         photo_2 = open('static/javoh 2.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo_2)
#     elif message.text.lower() ==  "akrom" or message.text.lower()=='акром':
#         photo = open('static/akrom.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo)
#     elif message.text.lower() ==  "nosir" or message.text.lower()=='носыр'or message.text.lower()=='носир':
#         photo = open('static/nosir.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo)
#     elif message.text.lower() ==  "asad" or message.text.lower()=='асад':
#         photo = open('static/asad.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo)
#     else:
#         tb.send_message(message.chat.id,"idi naxuy")



@tb.message_handler(commands=['start'])
def start(message):
    tb.send_location(message.chat.id.lat.lon)
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     button_1 = types.KeyboardButton('Жавохир')
#     button_2 = types.KeyboardButton('Акром')
#     button_3 = types.KeyboardButton('Носыр')
#     button_4 = types.KeyboardButton('Сардор')
#     button_5 = types.KeyboardButton('Асад')
#     button_6 = types.KeyboardButton('Жахонгир')
#     markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
#     but = types.InlineKeyboardMarkup()
#     but.add(types.InlineKeyboardButton("Коаппакчани уринг амаки",url= 'https://ru.sex-studentki.fun/hq-porn'))
#     but.add(types.InlineKeyboardButton("Коаппакчани уринг амаки", url='https://wel.ebalovo.porn/sites/deeper/'))
#     but.add(types.InlineKeyboardButton("Коаппакчани уринг амаки", url='http://i21.demonhd.net/main/'))
#     but.add(types.InlineKeyboardButton("Коаппакчани уринг амаки", url='https://xhdporno.tube/'))
#     tb.send_message(message.chat.id,f'здравствуйте{message.from_user.first_name}',reply_markup=markup)
#     tb.send_message(message.chat.id,':)',reply_markup=but)
#
# @tb.message_handler(content_types=['text'])
# def buttons(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
#     button_1=types.KeyboardButton('Жавохир')
#     button_2=types.KeyboardButton('Акром')
#     button_3 = types.KeyboardButton('Носыр')
#     button_4 = types.KeyboardButton('Сардор')
#     button_5 = types.KeyboardButton('Асад')
#     button_6 = types.KeyboardButton('Жахонгир')
#     markup.add(button_1,button_2,button_3,button_4,button_5,button_6)
#     if message.text == 'Жавохир':
#         photo_2 = open('static/javoh 2.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo_2)
#         javoh = types.InlineKeyboardMarkup()
#         javoh.add(types.InlineKeyboardButton('Инстаграм Жавохира ',url='https://instagram.com/_javokh.17'))
#         tb.send_message(message.chat.id,'⬇️⬇️⬇️⬇️⬇️⬇️⬇️',reply_markup=javoh)
#     elif message.text == 'Акром':
#         photo_3 = open('static/akrom-4.jpg', 'rb')
#         tb.send_photo(message.chat.id,photo_3)
#         akrom = types.InlineKeyboardMarkup()
#         akrom.add(types.InlineKeyboardButton('Инстаграм Акрома ',url='https://instagram.com/cicader.a'))
#         tb.send_message(message.chat.id,'⬇️⬇️⬇️⬇️⬇️⬇️⬇️',reply_markup=akrom)
#     elif message.text == 'Носыр':
#         photo_2 = open('static/nosir mello.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo_2)
#         nosir = types.InlineKeyboardMarkup()
#         nosir.add(types.InlineKeyboardButton('Инстаграм Носыра ',url='https://instagram.com/2ndchss'))
#         tb.send_message(message.chat.id, '⬇️⬇️⬇️⬇️⬇️⬇️⬇️',reply_markup=nosir)
#     elif message.text == 'Сардор':
#         photo = open('static/sardorbek.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo)
#         sardor = types.InlineKeyboardMarkup()
#         sardor.add(types.InlineKeyboardButton('Инстаграм Сардора ',url='https://instagram.com/sardor_vko'))
#         tb.send_message(message.chat.id,'⬇️⬇️⬇️⬇️⬇️⬇️⬇️',reply_markup=sardor)
#     elif message.text == 'Асад':
#         photo = open('static/asad.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo)
#         asad = types.InlineKeyboardMarkup()
#         asad.add(types.InlineKeyboardButton('Инстаграм Асада ',url='https://instagram.com/00.angel.of.death.00'))
#         tb.send_message(message.chat.id,'⬇️⬇️⬇️⬇️⬇️⬇️⬇️',reply_markup=asad)
#     elif message.text == 'Жахонгир':
#         photo = open('static/jahonchik.jpg', 'rb')
#         tb.send_photo(message.chat.id, photo)
#     else:
#         tb.send_message(message.chat.id, 'idi naxuy')
tb.polling(none_stop=True)