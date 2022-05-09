import ast
from Authentification import req, one_task
import json
from io import BytesIO

def loadMessage(msg):
    """
    Данный метод принимает на вход сообщение (msg) типа str, которое
    является запросом, содержит XML файл,
    После процедуры парсинга, извлкекаем хранящяяся параметры
    и вызываем нужный обработчик в зависимоти от параметра 'method'
    *пересмотреть*
    Доступные методы:
        'get':
            запрос на получение данных из коллекции "collectionName",
            удовлетворяющих фильтру "filter";
        put:
            запрос на добавление данных "data"
            в коллекцию "collectionName";
        delete:
            запрос на удаление данных из коллекции "collectionName",
            удовлетворяющих фильтру "filter";
        getLastData:
            запрос почледней строки данных из коллекции (дан id физического объекта)
        logIn:
            запрос на аутентификацию пользователя
            (проверка логина и пароля на соответствие);
    :param msg: запрос от клиента, который нужно обработать - тип str
    :return: ответ с сервера в виде сообщения типа str, которое содержит JSON объект
            на результат выполнения запроса.
    """
    try:
        msg = ast.literal_eval(msg)
        methodJSON = msg["method"]
        if methodJSON == "getData":
            print(msg)
            taskId=msg["task_id"]
            name_task=msg["tasks"]
            result = req(taskId, name_task)
            resultData = result

        elif methodJSON == "howLen":
            msgTasks=msg["tasks"]
            #print(msgLen)
            for json_obj in msgTasks:
                result = one_task(json_obj)
            resultData = result
        else:
            resultData = "Wrong Method"


        return responseJSON(resultData)
    except ImportError:
        # old
        result = "Wrong Request"
        return responseJSON(result)


# ответ на запрос
def responseJSON(data):
    """
    Формирует из данных "data" ответ клиенту
    :param data: принимает на вход данные, которые нужно передать тип str с JSON объектом внутри
    :return: сформированное сообщение, готовое к отправке клиенту
    """
    msg = {}
    msg["method"] = "response"
    msg["data"] = data
    msg=json.dumps(msg, indent=2).encode('utf-8')
    file_msg = BytesIO(msg)
    print(msg)
    return file_msg.getvalue()
