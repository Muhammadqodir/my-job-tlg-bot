import requests
import json

def search(text):
	r = requests.get('https://api.hh.ru/vacancies?text="тест"')
	return json.loads(r.text)
	pass