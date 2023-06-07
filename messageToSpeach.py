from io import BytesIO
import telebot
from gtts import gTTS
import re

TOKEN = "*******YOUR_TOKEN*******"


bot = telebot.TeleBot(TOKEN)


def converter_text(text: str) -> BytesIO:
    bytes_file = BytesIO()
    audio = gTTS(text=text, lang="ru")
    audio.write_to_fp(bytes_file)
    bytes_file.seek(0)
    return bytes_file


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        f"Привет, {message.from_user.first_name}! Я бот, который может перевести текст в речь. Напишите текст, и я переведу его в речь! \n\nℹ️ Для информации вызовите /help",
    )


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(
        message,
        "Чтобы перевести текст в речь, напишите мне текст, который нужно перевести в речь.\nДля использования бота, вызовите /start.",
    )


@bot.message_handler(func=lambda message: True)
def text_to_speech(message):
    if re.match(": | ! | ;", message.text):
        bot.reply_to(message, "Некорректные данные")
    else:
        voice = converter_text(message.text)
        bot.send_voice(message.from_user.id, voice)


bot.polling()
