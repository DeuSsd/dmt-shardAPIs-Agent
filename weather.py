import requests, json
from datetime import datetime
start_time = "2022-01-01" + "T00:00:00"
end_time  = "2022-01-10" + "T00:00:00"
location = "Vologda"


url = "https://visual-crossing-weather.p.rapidapi.com/history"

querystring = {"startDateTime": start_time,"aggregateHours":"24","location": location,"endDateTime": end_time,
               "unitGroup":"us","contentType":"json","shortColumnNames":"1"}

headers = {
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
	"X-RapidAPI-Key": "f1995b5d42msh6f6b019c97da73ap1301abjsn7decf230ad2e"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response = json.loads(response.text)

values = response.get('locations').get(location).get('values')

result = {}
for day in values:
	day_date = datetime.fromtimestamp(day.get('datetime')/1000)
	# print(day_date.strftime("%m/%d/%Y"), end = "   ")
	# print(day.get('temp'))
	result[day_date.strftime("%m/%d/%Y")] = day.get('temp')

print(result)