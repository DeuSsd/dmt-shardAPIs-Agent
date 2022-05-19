import connect_with_sql
def req(name,parameters):
    result = {
        "name":name,
        "parameters": parameters,
        "data": 123
    }
    return result

def one_task(task):
    web=task['website']
    param=task['parameters']
    date=param['date']
    res=date+str(' done')
    return {'web': web, 'parameters': {'date': date, 'data': res}}

def get_web_from_name(task):
    api=task['api']
    web=connect_with_sql.get_web(api)
    param=task['parameters']
    return {'website': web, 'parameters': param}

def get_name_from_web(task):
    api=task['web']
    web=connect_with_sql.get_web(api)
    param=task['parameters']
    return {'website': web, 'parameters': param}