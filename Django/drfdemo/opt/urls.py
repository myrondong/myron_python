
from django.urls import path, include, re_path
from . import views




urlpatterns = [
    path('exmple/',views.ExampleView.as_view()),
    path('home/',views.HomeView.as_view()),
    path('home/info/', views.HomeView.as_view()),
    re_path('student/(?P<pk>\d+)/', views.StudentInfoApiView.as_view()),
    path('demo1/', views.Demo1APiView.as_view()),
    path('demo2/', views.Demo2APiView.as_view()),
    path('demo3/', views.Demo3APiView.as_view()),
    path('demo4/', views.Demo4APiView.as_view()),
    path('demo5/', views.Demo5APiView.as_view()),
    path('demo6/', views.Demo6APiView.as_view()),
]
