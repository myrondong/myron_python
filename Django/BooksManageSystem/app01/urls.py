from django.contrib import admin
from django.urls import path
from django.urls import include
from app01 import views

urlpatterns = [
    path('add_publish', views.add_publish),
    path('publish_list', views.publish_list)
]
