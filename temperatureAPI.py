import requests, json
from datetime import datetime

class temperatureAPI():
    def __init__(self, params, config):
        self.start_time = params[0].get("value") + "T00:00:00"
        self.end_time = params[1].get("value") + "T00:00:00"
        self.location = params[2].get("value")

        self.querystring = {"startDateTime": self.start_time, "aggregateHours": "24", "location": self.location,
                       "endDateTime": self.end_time,
                       "unitGroup": "us", "contentType": "json", "shortColumnNames": "1"}

        self.headers = {
            "X-RapidAPI-Host": config.get("rapid_host"),
            "X-RapidAPI-Key": config.get("rapid_key")
        }

        self.response = requests.request("GET", config.get("website"), headers=self.headers, params=self.querystring)
        self.response = json.loads(self.response.text)

    def get(self):
        self.values = self.response.get('locations').get(self.location).get('values')
        self.date, self.value = [], []
        for day in self.values:
            day_date = datetime.fromtimestamp(day.get('datetime') / 1000)
            self.date.append(day_date.strftime("%m/%d/%Y"))
            self.value.append(day.get('temp'))

        return self.date, self.value
