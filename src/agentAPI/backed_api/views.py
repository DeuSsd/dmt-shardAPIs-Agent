from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import APIData
from .serializer import APISerializer

class RESTAPIView(APIView):
    def get(self, request):
        lst = APIData.objects.all().values()
        print(request.data)
        api = request.data['api']
        parameters_api = request.data['param']
        date_api=parameters_api['date']
        loc_api=parameters_api['location']
        return Response({'api': api, 'param':{'date': date_api,'location': loc_api, 'data': 123}})
        #return Response({'title': 'GO OUT!!!'})#для вызова из браузера

    def post(self,request):
        post_new=APIData.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})



#class WomenAPIView(generics.ListAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
