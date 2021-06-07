def getVacancies(arr):
	res = []
	for x in range(0,20):
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
		res_str = name+"\nКомпания: "+company+"\nТребования: "+requirement+"\nЗарплата: "+salary+"\nГрафик работы: "+schedule+"\n"+url
		res.append(res_str)
		pass
		return arr
	pass