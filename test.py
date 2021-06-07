import telebot
import config
import api
import parser

res = api.search("тест")
arr = parser.getVacancies(res)

print(arr)