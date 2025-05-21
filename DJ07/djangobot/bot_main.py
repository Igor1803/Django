import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
import requests
import logging

# Логирование
logging.basicConfig(level=logging.INFO)

# Настройки
API_URL = "http://127.0.0.1:8000/api"
BOT_TOKEN = "7961846850:AAFhaBZNWcTe_lYPsKIrUUbha_pKcVYMbVg"

bot = telebot.TeleBot(BOT_TOKEN)

# Установка команд для системного меню Telegram (три полоски)
bot.set_my_commands([
    telebot.types.BotCommand("start", "Регистрация"),
    telebot.types.BotCommand("myinfo", "Мои данные"),
    telebot.types.BotCommand("help", "Помощь"),
])

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_command(message: Message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username
    }

    # Клавиатура с кнопками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("/myinfo"), KeyboardButton("/help"))

    try:
        response = requests.post(f"{API_URL}/register/", json=data)
        if response.status_code == 201:
            bot.send_message(message.chat.id, "✅ Вы успешно зарегистрированы!", reply_markup=keyboard)
        elif response.status_code == 200:
            bot.send_message(message.chat.id, "ℹ️ Вы уже зарегистрированы!", reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, f"❌ Ошибка регистрации! Код: {response.status_code}", reply_markup=keyboard)
            print(response.text)  # Для отладки
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка подключения к серверу: {e}", reply_markup=keyboard)

# Обработчик команды /myinfo
@bot.message_handler(commands=['myinfo'])
def user_info(message: Message):
    try:
        response = requests.get(f"{API_URL}/user/{message.from_user.id}/")
        if response.status_code == 200:
            user_data = response.json()
            bot.reply_to(message, f"Ваши данные:\nID: {user_data['user_id']}\nUsername: {user_data['username']}")
        elif response.status_code == 404:
            bot.send_message(message.chat.id, "Вы не зарегистрированы!")
        else:
            bot.send_message(message.chat.id, "Ошибка при получении данных!")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка подключения к серверу: {e}")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help_command(message: Message):
    help_text = (
        "📋 Доступные команды:\n"
        "/start — регистрация\n"
        "/myinfo — информация о пользователе\n"
        "/help — помощь"
    )
    bot.send_message(message.chat.id, help_text)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
