import telebot
import config
import api
import parser

res = api.search("ัะตัั")
arr = parser.getVacancies(res)

print(arr)