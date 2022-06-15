from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("students/",views.StudentAPIView.as_view()),
    path("studentsDj/",views.StudentDjView.as_view())
]
