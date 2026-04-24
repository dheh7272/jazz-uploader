import os
import telebot
import requests

# Secrets se Token uthana
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_id_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalam-o-Alaikum Kareem bhai! Main Sukuna hoon. Mujhe Jazz Number ya Video Link bhejain, main foran kaam shuru kar doonga.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg_text = message.text
    
    if "03" in msg_text and len(msg_text) == 11:
        bot.reply_to(message, f"Theek hai, main {msg_text} par OTP bhej raha hoon...")
        # Yahan hum Jazz login ka function call karenge
    
    elif "http" in msg_text:
        bot.reply_to(message, "Link mil gaya! Main downloading aur uploading shuru kar raha hoon...")
        # Yahan hum downloading/uploading ka code chalayenge
    
    else:
        bot.reply_to(message, "Kareem bhai, mujhe sahi number ya link bhejain please.")

print("Sukuna is listening...")
bot.infinity_polling()
