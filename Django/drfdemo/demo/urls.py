from django.contrib import admin
from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path("students/",views.StudentApiView.as_view()),

    # re_path 就是path 上可以使用正则表达式
    re_path("^students/(?P<pk>[0-9]+)/$",views.StudentInfoApiView.as_view()),

    path("gstudents/",views.StudentGenericAPIView.as_view()),
]
