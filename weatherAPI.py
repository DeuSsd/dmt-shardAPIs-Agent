import requests, json
from datetime import datetime

class weatherAPI():
    def __init__(self, params):
        self.start_time = params.get("start_time") + "T00:00:00"
        self.end_time = params.get("end_time") + "T00:00:00"
        self.location = params.get("location")
        self.url = "https://visual-crossing-weather.p.rapidapi.com/history"

        self.querystring = {"startDateTime": self.start_time, "aggregateHours": "24", "location": self.location,
                       "endDateTime": self.end_time,
                       "unitGroup": "us", "contentType": "json", "shortColumnNames": "1"}

        self.headers = {
            "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
            "X-RapidAPI-Key": "f1995b5d42msh6f6b019c97da73ap1301abjsn7decf230ad2e"
        }

        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        self.response = json.loads(self.response.text)

    def get(self):
        self.values = self.response.get('locations').get(self.location).get('values')
        self.result = {}
        for day in self.values:
            day_date = datetime.fromtimestamp(day.get('datetime') / 1000)
            self.result[day_date.strftime("%m/%d/%Y")] = day.get('temp')

        return self.result
