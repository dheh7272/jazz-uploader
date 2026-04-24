import os
import telebot

# GitHub Secrets se Token uthana
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Is line ko main ne theek kar diya hai (message_handler)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalam-o-Alaikum Kareem bhai! Main Sukuna hoon. Mujhe Jazz Number ya Video Link bhejain, main foran kaam shuru kar doonga.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg_text = message.text
    
    if msg_text.startswith("03") and len(msg_text) == 11:
        bot.reply_to(message, f"Theek hai, main {msg_text} par OTP bhej raha hoon... (Process Start)")
    
    elif "http" in msg_text:
        bot.reply_to(message, "Link mil gaya! Downloading aur Uploading shuru ho rahi hai...")
    
    else:
        bot.reply_to(message, "Kareem bhai, mujhe sahi number ya link bhejain please.")

print("Sukuna is listening...")
bot.infinity_polling()
