from django.contrib import admin
from django.urls import path, include
from mobile.views import index
urlpatterns = [
    path('', index.index, name='mobile_index'),
]