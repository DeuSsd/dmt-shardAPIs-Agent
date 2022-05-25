import shardAPI

def one_task(test_api):
    api=test_api['api']
    web=test_api['website']
    if api=='sunsetAPI' or api=='sunriseAPI':
        type_val='time'
    else:
        type_val='float'
    req=shardAPI.response(test_api)
    req_date=req['date']
    list_date=[]
    list_values=[]
    #print(type(req['value'][1]))
    for i in range(len(req_date)):
        res_date={'id':i+1, 'value': str(req['date'][i])}
        list_date.append(res_date)
        res_values={'id':i+1, 'value':str(req['value'][i])}
        list_values.append(res_values)
    finish_response1={'parameter_name': 'current_time', 'type':'date','values': list_date}
    finish_response2={'parameter_name': 'data', 'type': type_val,'values': list_values}
    list_finish=[finish_response1, finish_response2]
    return {'api': api, 'parameters': list_finish}

#a=one_task(test_api_temperature)
#print(a)

def change_date(date):
    new_date=str(date[6:10]+"-"+date[3:5]+"-"+date[0:2])
    return new_date

# a="24/08/1999"
# b=change_date(a)
# print(b)