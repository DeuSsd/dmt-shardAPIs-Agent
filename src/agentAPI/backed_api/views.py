from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
#from .models import APIData
from .models import APIWEB
from .main import one_task, get_web_from_name
import connect_with_sql
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
        return Response({'apis': list_api_param})


class RESTAPIView2(APIView):
    def post(self, request):
        task_id = request.data['task_id']
        user_id = request.data['user_id']
        some_api = request.data['APIs']
        list_api_param = []
        for i in range(len(some_api)):
            param = connect_with_sql.get_param(i + 1)
            title = connect_with_sql.get_title(i + 1)
            api = {'title': title[0][0], 'api': some_api[i], 'description': title[0][1]}
            api = {'api': api, 'parameters': param}
            # parameter={'parameters':param}
            list_api_param.append(api)
        return Response({'task_id': task_id, 'user_id': user_id, 'tasks': list_api_param})

class RESTAPIView3(APIView):
    def post(self, request):
        list_res = []
        task_id = request.data['task_id']
        user_id = request.data['user_id']
        tasks = request.data['tasks']
        for k in range(len(tasks)):
            res = get_web_from_name(tasks[k])  # получил ссылку на отдельный АПИ
            request_to_anton = one_task(res)  # это я отправляю Антону JSON с ссылкой и параметрами и получаю от него ответ
            web_api = connect_with_sql.from_web_to_api(request_to_anton['web'])  # заменяю в ответе Антона ссылку на название АПИ
            request_to_user = {'api': web_api,'data': [request_to_anton['parameters']]}  # формирую ответ из названия АПИ и его данных
            list_res.append(request_to_user)
        return Response({'task_id': task_id, 'user_id': user_id, 'task_data': list_res})