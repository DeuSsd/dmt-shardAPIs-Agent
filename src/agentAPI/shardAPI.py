import json
from datetime import datetime

class shardAPI():

    def __init__(self, task):
        self.config = {}
        self.config["website"] = task.get("website")
        self.config["rapid_host"] = task.get("X-RapidAPI-Host")
        self.config["rapid_key"] = task.get("X-RapidAPI-Key")
        self.params = task.get("parameters")
        self.api = task.get("api")

    def execute(self):
        module = __import__(self.api)
        class_ = getattr(module, self.api)
        date, value = class_(self.params, self.config).get()
        result_dict = {
                    "date": date,
                    "value": value
                   }
        self.result = result_dict

    def get(self):
        self.execute()
        return self.result

# shard_moscow_weather = shardAPI(test_api_weather).get()
#shard_moscow_temperature = shardAPI(test_api_sunrise).get()
#print(shard_moscow_temperature)
def response(test_api):
    shard_moscow_humidity = shardAPI(test_api).get()
    return shard_moscow_humidity
