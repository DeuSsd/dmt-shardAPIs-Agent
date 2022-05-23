"""agentAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backed_api.views import RESTAPIView,RESTAPIView2,RESTAPIView3
from backed_api.views import *

#urlpatterns = [path('admin/', admin.site.urls),path('api/v1/womenlist/', WomenAPIView.as_view())]
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/apis/', include('backed_api.urls'))
    path('api/getall/', RESTAPIView.as_view()),
    path('api/parameters/', RESTAPIView2.as_view()),
    path('api/data/', RESTAPIView3.as_view()),
]