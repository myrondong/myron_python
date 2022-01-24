from django.contrib import admin
from django.urls import path, include
from web.views import index
urlpatterns = [
    path('', index.index, name='web_index'),

]