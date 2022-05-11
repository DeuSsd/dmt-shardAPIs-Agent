# from weather_class import WeatherAPI
import json

class shardAPI():

    def __init__(self, task_id: str, task):
        self.task_id = task_id
        self.api = task.get("api")
        self.params = task.get("parameters")
        self.execute()

    def execute(self):
        module = __import__(self.api)
        class_ = getattr(module, self.api)
        record = class_(self.params).get()
        result_dict = {
                    "task_id": self.task_id,
                    "api_data":json.dumps(record)
                   }
        self.result = json.dumps(result_dict)

        # self.parameters = task.get("parameters")
        # self.execute()

    # def execute(self):
    #     if self.api == "weatherAPI":
    #         self.execute_weather()


    # def execute_weather(self):
    #     record = WeatherAPI(self.parameters.get("start_time"),
    #                              self.parameters.get("end_time"),
    #                              self.parameters.get("location")).get()
    #     result_dict = {
    #         "task_id": self.task_id,
    #         "api_data":json.dumps(record)
    #        }
    #
    #     self.result = json.dumps(result_dict)

    def get(self):
        return self.result



task1 = {"api": "weatherAPI",
         "parameters": {
                        "start_time": "2022-01-01",
                        "end_time": "2022-01-15",
                        "location": "Vologda"
         }
    }

# task2 = {"api": "weatherAPI",
#          "parameters": {
#                         "start_time": "2022-01-01",
#                         "end_time": "2022-01-05",
#                         "location": "Moscow"
#          }
#     }
shard1 = shardAPI('123123', task1).get()
# shard2 = shardAPI('1231423', task2).get()
# first_api = WeatherAPI("2022-01-01", "2022-01-15", "Moscow")
# res = first_api.get()
# res = json.dumps(res)



print("")
