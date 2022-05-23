import json

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
        self.result = json.dumps(result_dict)

    def get(self):
        self.execute()
        return self.result


test_api_temperature={
    'api': "temperatureAPI",
    'website': 'https://visual-crossing-weather.p.rapidapi.com/history',
    "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
    "X-RapidAPI-Key": "f1995b5d42msh6f6b019c97da73ap1301abjsn7decf230ad2e",
    'parameters': [
        {'parameter': 'start_time',
         'type': 'time',
         'value': '2022-01-01'
         },
         {'parameter': 'end_time',
          'type': 'time',
          'value': '2022-01-15'
          },
         {'parameter': 'location',
          'type': 'string',
          'value': 'Moscow'
          }
    ]
}
test_api_humidity={
    'api': "humidityAPI",
    'website': 'https://visual-crossing-weather.p.rapidapi.com/history',
    "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
    "X-RapidAPI-Key": "f1995b5d42msh6f6b019c97da73ap1301abjsn7decf230ad2e",
    'parameters': [
        {'parameter': 'start_time',
         'type': 'time',
         'value': '2022-01-01'
         },
         {'parameter': 'end_time',
          'type': 'time',
          'value': '2022-01-15'
          },
         {'parameter': 'location',
          'type': 'string',
          'value': 'Moscow'
          }
    ]
}

test_api_sunrise={
    'api': "sunriseAPI",
    'website': "https://sunrise-sunset-times.p.rapidapi.com/getSunriseAndSunset",
    "X-RapidAPI-Host": "sunrise-sunset-times.p.rapidapi.com",
    "X-RapidAPI-Key": "f1995b5d42msh6f6b019c97da73ap1301abjsn7decf230ad2e",
    'parameters': [
        {'parameter': 'start_time',
         'type': 'time',
         'value': '2022-01-01'
         },
         {'parameter': 'end_time',
          'type': 'time',
          'value': '2022-01-15'
          },
         {'parameter': 'latitude',
          'type': 'float',
          'value': '55.7558'
          },
        {'parameter': 'longitude',
          'type': 'float',
          'value': '37.6173'
          }
    ]
}
test_api_sunset={
    'api': "sunsetAPI",
    'website': "https://sunrise-sunset-times.p.rapidapi.com/getSunriseAndSunset",
    "X-RapidAPI-Host": "sunrise-sunset-times.p.rapidapi.com",
    "X-RapidAPI-Key": "f1995b5d42msh6f6b019c97da73ap1301abjsn7decf230ad2e",
    'parameters': [
        {'parameter': 'start_time',
         'type': 'time',
         'value': '2022-01-01'
         },
         {'parameter': 'end_time',
          'type': 'time',
          'value': '2022-01-15'
          },
         {'parameter': 'latitude',
          'type': 'float',
          'value': '55.7558'
          },
        {'parameter': 'longitude',
          'type': 'float',
          'value': '37.6173'
          }
    ]
}
# shard_moscow_weather = shardAPI(test_api_weather).get()
shard_moscow_humidity = shardAPI(test_api_humidity).get()



print(shard_moscow_humidity)
