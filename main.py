import telebot
import dbworker
import config
import time
from telebot import types
from config import T

bot = telebot.TeleBot(T)
qs = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я, искусственный интеллект Валли!'
                                      '\nДавай познакомимся! Как как тебя зовут?')
    dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(
    func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_number(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text='Начать игру', callback_data='Start')
    ]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Очень приятно!!! Нажми на кнопку, чтобы начать игру!', reply_markup=keyboard)
    dbworker.set_state(message.chat.id, config.States.S_START.value)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Start':
        buttons = [
            types.InlineKeyboardButton(text='1. Голосовой помощник', callback_data='T1'),
            types.InlineKeyboardButton(text='2. Леонардо да Винчи', callback_data='F1'),
            types.InlineKeyboardButton(text='3. Яблоко', callback_data='F1'),
            types.InlineKeyboardButton(text='4. Пизанская башня', callback_data='F1')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='ИГРА!!!')
        time.sleep(1.5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Правила: ответь на все вопросы! Поехали!')
        time.sleep(1.5)
        file = open('1.png', 'rb')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_photo(call.message.chat.id, file, f"Что из этого относится к искуственному интеллекту?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'F1':
        qs[call.message.chat.id, "q1"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(text='1990', callback_data='F2'),
            types.InlineKeyboardButton(text='1998', callback_data='F2'),
            types.InlineKeyboardButton(text='1983', callback_data='F2'),
            types.InlineKeyboardButton(text='1980', callback_data='T2')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('2.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"В каком году были созданы первые роботы?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'T1':
        qs[call.message.chat.id, "q1"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(text='1990', callback_data='F2'),
            types.InlineKeyboardButton(text='1998', callback_data='F2'),
            types.InlineKeyboardButton(text='1983', callback_data='F2'),
            types.InlineKeyboardButton(text='1980', callback_data='T2')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('2.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"В каком году были созданы первые роботы?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'F2':
        qs[call.message.chat.id, "q2"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(text='Корпорацию Open Office', callback_data='F3'),
            types.InlineKeyboardButton(text='Корпорацию Microsoft', callback_data='T3'),
            types.InlineKeyboardButton(text='Корпорацию Adobe Reader', callback_data='F3'),
            types.InlineKeyboardButton(text='Телеграм', callback_data='F3')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"Что создал Билл Гейтс?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'T2':
        qs[call.message.chat.id, "q2"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(text='Корпорацию Open Office', callback_data='F3'),
            types.InlineKeyboardButton(text='Корпорацию Microsoft', callback_data='T3'),
            types.InlineKeyboardButton(text='Корпорацию Adobe Reader', callback_data='F3'),
            types.InlineKeyboardButton(text='Телеграм', callback_data='F3')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"Что создал Билл Гейтс?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'T3':
        qs[call.message.chat.id, "q3"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(text='Asus', callback_data='F4'),
            types.InlineKeyboardButton(text='Lenovo', callback_data='F4'),
            types.InlineKeyboardButton(text='Huawei', callback_data='F4'),
            types.InlineKeyboardButton(text='Apple', callback_data='T4')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('4.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"Директором какой компании был Стив Джобс?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'F3':
        qs[call.message.chat.id, "q3"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(text='Asus', callback_data='F4'),
            types.InlineKeyboardButton(text='Lenovo', callback_data='F4'),
            types.InlineKeyboardButton(text='Apple', callback_data='T4'),
            types.InlineKeyboardButton(text='Huawei', callback_data='F4')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('4.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"Директором какой компании был Стив Джобс?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'F4':
        qs[call.message.chat.id, "q4"] = '0 баллов'
        buttons = [
            types.InlineKeyboardButton(text='City Plaza', callback_data='F5'),
            types.InlineKeyboardButton(text='Сириус', callback_data='T5'),
            types.InlineKeyboardButton(text='Сочи', callback_data='F5'),
            types.InlineKeyboardButton(text='Сочи Парк', callback_data='F5')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('5.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"Как называется первая федеральная территория в России, "
                                                   f"которая раньше находилась в Адлерском районе?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'T4':
        qs[call.message.chat.id, "q4"] = '1 балл'
        buttons = [
            types.InlineKeyboardButton(text='City Plaza', callback_data='F5'),
            types.InlineKeyboardButton(text='Сириус', callback_data='T5'),
            types.InlineKeyboardButton(text='Сочи', callback_data='F5'),
            types.InlineKeyboardButton(text='Сочи Парк', callback_data='F5')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('5.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, f"Как называется первая федеральная территория в России, "
                                                   f"которая раньше находилась в Адлерском районе?",
                       reply_markup=keyboard)
        file.close()

    if call.data == 'T5':
        qs[call.message.chat.id, "q5"] = '1 балл'
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, f'Ура, тест успешно завершен. Идет подсчет баллов! Твои ответы:'
                                               f'\n\n1. Вопрос - {qs[call.message.chat.id, "q1"]}'
                                               f'\n2. Вопрос - {qs[call.message.chat.id, "q2"]}'
                                               f'\n3. Вопрос - {qs[call.message.chat.id, "q3"]}'
                                               f'\n4. Вопрос - {qs[call.message.chat.id, "q4"]}'
                                               f'\n5. Вопрос - {qs[call.message.chat.id, "q5"]}')

        time.sleep(1.5)
        bot.send_message(call.message.chat.id, f'Ты Молодец!!!')
        time.sleep(2.5)
        bot.send_message(call.message.chat.id, f'До новых встреч!')
        time.sleep(1.5)
        bot.send_message(call.message.chat.id, f'Пока!')

    if call.data == 'F5':
        qs[call.message.chat.id, "q5"] = '0 баллов'
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, f'Ура, тест успешно завершен. Идет подсчет баллов! Твои ответы:'
                                   f'\n\n1. Вопрос - {qs[call.message.chat.id, "q1"]}'
                                   f'\n2. Вопрос - {qs[call.message.chat.id, "q2"]}'
                                   f'\n3. Вопрос - {qs[call.message.chat.id, "q3"]}'
                                   f'\n4. Вопрос - {qs[call.message.chat.id, "q4"]}'
                                   f'\n5. Вопрос - {qs[call.message.chat.id, "q5"]}')

        time.sleep(1.5)
        bot.send_message(call.message.chat.id, f'Ты Молодец!!!')
        time.sleep(2.5)
        bot.send_message(call.message.chat.id, f'До новых встреч!')
        time.sleep(1.5)
        bot.send_message(call.message.chat.id, f'Пока!')


bot.polling(none_stop=True, interval=0)
