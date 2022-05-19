from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import APIData
from .main import one_task, get_web_from_name
import connect_with_sql
from .serializer import APISerializer

class RESTAPIView(APIView):
    def get(self, request):
        #print(request.data)
        if request.data == {}:
            return Response({'title': 'GO OUT!!!'})  # для вызова из браузера
        if request.data['request']=='get_api':
            list_api_param=[]
            apis=connect_with_sql.get_API()
            for i in range(len(apis)):
                res=connect_with_sql.get_param(i+1)
                api={'api': apis[i],'parameters':res}
                list_api_param.append(api)
            print(list_api_param)
            return Response({'apis':list_api_param})
        if request.data['request']=='get_data':
            list_res=[]
            task_id = request.data['task_id']
            user_id = request.data['user_id']
            tasks = request.data['tasks']
            for k in range(len(tasks)):
                res=get_web_from_name(tasks[k])#получил ссылку на отдельный АПИ
                request_to_anton=one_task(res)#это я отправляю Антону JSON с ссылкой и параметрами и получаю от него ответ
                web_api=connect_with_sql.from_web_to_api(request_to_anton['web'])#заменяю в ответе Антона ссылку на название АПИ
                #print(web_api)
                #print(request_to_anton)
                request_to_user={'api': web_api,'parameters':request_to_anton['parameters']}#формирую ответ из названия АПИ и его данных
                list_res.append(request_to_user)

            #return Response(list_res)
            return Response({'task_id':task_id,'user_id': user_id, 'tasks':list_res})


    def post(self, request):
        post_new=APIData.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
