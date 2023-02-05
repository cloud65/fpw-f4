"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers

from eda.views import CategoriesViewSet, EdaViewSet, get_image, get_index_page
from main.swagger import get_swagger_url
from main.userapi import UserViewSet

router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'eda', EdaViewSet)

#https://habr.com/ru/company/otus/blog/583220/

urlpatterns = [
    path("", get_index_page),
    path('api/', include(router.urls)),
    path('api/image/<str:guid>', get_image),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + get_swagger_url()
