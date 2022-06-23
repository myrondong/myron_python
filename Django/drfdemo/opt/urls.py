
from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('exmple/',views.ExampleView.as_view()),
    path('home/',views.HomeView.as_view()),
    path('home/info/', views.HomeView.as_view())
]
