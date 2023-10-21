
import telebot


bot = telebot.TeleBot('5643344102:AAES3oQlVGyLi01T7OnBaCGHYpY9aNK2f24')

@bot.message_handler(Commands={"start"})
def start(m, res=False):
    bot.send_message(m.chat.id, 'Напишите мне что-то')
