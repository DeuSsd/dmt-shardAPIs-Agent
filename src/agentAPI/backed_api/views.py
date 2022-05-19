from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import APIData
from .main import one_task
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
            k=0
            while k<len(tasks):
                res=one_task(tasks[k])
                list_res.append(res)
                k=k+1
            return Response({'task_id':task_id,'user_id': user_id, 'tasks':list_res})


    def post(self, request):
        post_new=APIData.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
