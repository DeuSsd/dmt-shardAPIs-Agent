import json
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
#from .models import APIData
from .models import APIWEB
from .main import one_task, get_web_from_name
import connect_with_sql
import Client
from django.http import HttpResponse
from .serializer import APISerializer

class RESTAPIView(APIView):
    def get(self, request):
        list_api_param = []
        apis = connect_with_sql.get_API()
        for i in range(len(apis)):
            res = connect_with_sql.get_title(i + 1)
            api = {'title': res[0][0],'api': apis[i], 'description': res[0][1]}
            list_api_param.append(api)
            ff = {'apis': list_api_param}
        return Response(json.dumps(ff), content_type="application/json")


class RESTAPIView2(APIView):
    def post(self, request):
        task_id = request.data['task_id']
        user_id = request.data['user_id']
        some_api = request.data['insides']
        list_api_param = []
        for i in range(len(some_api)):
            param = connect_with_sql.get_param(i + 1)
            title = connect_with_sql.get_title(i + 1)
            api = {'title': title[0][0], 'api': some_api[i], 'description': title[0][1]}
            api = {'api': api, 'parameters': param}
            # parameter={'parameters':param}
            list_api_param.append(api)
            ff = {'task_id': task_id, 'user_id': user_id, 'insides': list_api_param}
        return Response(json.dumps(ff), content_type="application/json")

class RESTAPIView3(APIView):
    def post(self, request):
        list_res = []
        task_id = request.data['task_id']
        user_id = request.data['user_id']
        tasks = request.data['insides']
        for k in range(len(tasks)):
            res = get_web_from_name(tasks[k])  # получил ссылку на отдельный АПИ
            request_to_shardAPI = Client.one_task(res)  # это я отправляю Антону JSON с ссылкой и параметрами и получаю от него ответ
            #web_api = connect_with_sql.from_web_to_api(request_to_shardAPI['web'])  # заменяю в ответе Антона ссылку на название АПИ
            #print('**********')
            #print(request_to_shardAPI['api'])
            response_to_user = {'api': request_to_shardAPI['api'],'data': request_to_shardAPI['parameters']}  # формирую ответ из названия АПИ и его данных
            list_res.append(response_to_user)
            ff = {'task_id': task_id, 'user_id': user_id, 'insides': list_res}
        return Response(json.dumps(ff), content_type="application/json")