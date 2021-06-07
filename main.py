import telebot
import config
from telebot import types

TOKEN = config.BOT_API

bot = telebot.TeleBot(TOKEN)

categorys = [
	"Автомобильный бизнес",
	"Банки",
	"Безопасность",
	"Бухгалтерия",
	"Менеджмент",
	"Домашний персонал",
	"Закупки",
	"Информационные технологии",
	"Консультирование",
	"Маркетинг",
	"Медицина",
	"Наука образование",
	"Рабочий персонал",
	"Страхование",
	"Транспорт",
	"Туризм",
	"Юристы"
]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "My Job Поиск ваканций")
	markup = types.ReplyKeyboardMarkup()
	search = types.KeyboardButton('Поиск 🔍')
	markup.row(search)
	for x in range(0,len(categorys)):
		item = types.KeyboardButton(categorys[x])
		markup.row(item)
		pass
	bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()