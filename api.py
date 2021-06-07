import requests
import json

def search(text):
	r = requests.get('https://api.hh.ru/vacancies?text="'+text+'"')
	return json.loads(r.text)
	pass