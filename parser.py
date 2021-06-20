def getVacancies(arr):
	res = []
	for x in range(0,len(arr["items"])):
		print(x)
		name = arr["items"][x]["name"]
		company = "Нет данных!"
		try:
			company = arr["items"][x]["department"]["name"]
			pass
		except Exception as e:
			pass
		requirement = "Нет данных!"
		try:
			requirement = arr["items"][x]["snippet"]["requirement"]
			pass
		except Exception as e:
			pass
		salary = "Нет данных!"
		try:
			salary = "от " + arr["items"][x]["salary"]["from"] + "руб. до" + arr["items"][x]["salary"]["to"]+"руб." 
			pass
		except Exception as e:
			pass
		schedule = "Нет данных!"
		try:
			schedule = arr["items"][x]["schedule"]["name"] 
			pass
		except Exception as e:
			pass
		url = arr["items"][x]["url"]
		try:
			res_str = "📌"+name+"\n\n🏢Компания: "+company+"\n\n‼️Требования: "+requirement+"\n\n💸Зарплата: "+salary+"\n\n🗓График работы: "+schedule+"\n\n"+"🔗Подробнее: "+url
			res.append(res_str)
			pass
		except Exception as e:
			pass
		
		pass
	return res
	pass