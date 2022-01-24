from django.contrib import admin
from django.urls import path, include
from myadmin.views import index
# 后台管理子路由
urlpatterns = [
    path('',index.index,name='myadmin_index'),

]