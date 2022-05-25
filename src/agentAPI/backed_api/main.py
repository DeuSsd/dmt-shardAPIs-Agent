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
    list_param=[]
    for i in range(len(param)):
        one_param=param[i]
        parameter=one_param['parameter']
        type=one_param['type']
        value=one_param['value']
        values=[{'value':value},{'value':value}]
        list_param.append({'parameter_name': parameter,'type': type,'values':values})
    return {'web': web, 'parameters': list_param}

def get_web_from_name(task):
    api=task['api']
    web=connect_with_sql.get_web(api)
    x_host=connect_with_sql.get_xhost(api)
    x_key=connect_with_sql.get_xkey(api)
    param=task['parameters']
    return {'api': api, 'website': web, "X-RapidAPI-Host": x_host, "X-RapidAPI-Key": x_key,'parameters': param}

def get_name_from_web(task):
    api=task['web']
    web=connect_with_sql.get_web(api)
    param=task['parameters']
    return {'website': web, 'parameters': param}