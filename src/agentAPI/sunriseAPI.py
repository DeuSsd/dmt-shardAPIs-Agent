import requests, json
from datetime import datetime, timedelta
import time

def change_date(date):
    new_date = str(date[6:10] + "-" + date[3:5] + "-" + date[0:2])
    return new_date

class sunriseAPI():
    def __init__(self, params, config):
        self.start_time = datetime.strptime(change_date(params[0].get("value")), '%Y-%M-%d').date()
        self.end_time = datetime.strptime(change_date(params[1].get("value")), '%Y-%M-%d').date()
        self.latitude = params[2].get("value")
        self.longitude = params[3].get("value")
        self.website = config.get("website")


        self.headers = {
            "X-RapidAPI-Host": config.get("rapid_host"),
            "X-RapidAPI-Key": config.get("rapid_key")
        }


    def get(self):
        self.date = []
        self.value = []
        init_date = self.start_time
        while init_date != self.end_time:
            self.querystring = {"date":str(init_date),"latitude":self.latitude,"longitude":self.longitude}
            self.response = requests.request("GET", self.website, headers=self.headers, params=self.querystring)
            self.response = json.loads(self.response.text)
            self.date.append(str(init_date.strftime('%d-%m-%Y')))
            self.value.append(self.response.get("sunrise")[11:16])
            init_date += timedelta(days = 1)
            time.sleep(1)
        return self.date, self.value
