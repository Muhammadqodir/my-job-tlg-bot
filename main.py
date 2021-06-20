import telebot
import config
from telebot import types
import api
import parser
import re

TOKEN = config.BOT_API

bot = telebot.TeleBot(TOKEN)

categorys = [
	"Автомобильный бизнес🚘",
	"Банки🏦",
	"Безопасность🛡",
	"Бухгалтерия💸",
	"Менеджмент🤵",
	"Домашний персонал👩‍🍳",
	"Закупки💍",
	"Информационные технологии👨‍💻",
	"Консультирование👨‍💼",
	"Маркетинг👩‍💼",
	"Медицина👨‍⚕️",
	"Наука образование👩‍🎓",
	"Рабочий персонал👷‍♂️",
	"Страхование👩‍💼",
	"Транспорт👮‍♂️",
	"Туризм✈️",
	"Юристы📃"
]

def deEmojify(text):
	regrex_pattern = re.compile(pattern = "["
		u"\U0001F600-\U0001F64F"  # emoticons
		u"\U0001F300-\U0001F5FF"  # symbols & pictographs
		u"\U0001F680-\U0001F6FF"  # transport & map symbols
		u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
		"]+", flags = re.UNICODE)
	return regrex_pattern.sub(r'',text)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "My Job Поиск ваканций")
	markup = types.ReplyKeyboardMarkup()
	search = types.KeyboardButton('Поиск 🔍')
	markup.row(search)
	markup.row(types.KeyboardButton('Создать резюме 📄'))
	markup.row(types.KeyboardButton('ЦССТ СКФУ ✅'))
	for x in range(0,len(categorys)):
		item = types.KeyboardButton(categorys[x])
		markup.row(item)
		pass
	bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "Создать резюме 📄":
		bot.send_message(message.chat.id, "Создание резюме – важнейший шаг в процессе поиска работы. Это твоя визитная карточка! От того, насколько грамотно оно будет составлено, во многом зависят твои шансы на получение желаемой должности. \n📄 Упростим задачу, всё что тебе необходимо, это перейти по ссылке и заполнить информацию о себе.\nhttps://docs.google.com/forms/d/e/1FAIpQLSd_P7B5YqJf53deCQvsE2hUAs-kLpXkNYs5rCKFZkiUlUeb-g/viewform")
	elif message.text == "ЦССТ СКФУ ✅":
		bot.send_message(message.chat.id, "@WorkNCFU_bot")
	else:
		res = api.search(deEmojify(message.text))
		arr = parser.getVacancies(res)
		for x in range(0,len(arr)):
			bot.send_message(message.chat.id, arr[x])
			pass

bot.polling()