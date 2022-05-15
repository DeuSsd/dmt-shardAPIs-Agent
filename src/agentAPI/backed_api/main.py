def req(name,parameters):
    result = {
        "name":name,
        "parameters": parameters,
        "data": 123
    }
    return result

def one_task(task):
    api=task['api']
    param=task['parameters']
    date=param['date']
    res=date+str(' done')
    return {'api': api, 'parameters': {'date': date, 'data': res}}