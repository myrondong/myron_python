from django.urls import re_path, path
from . import views

urlpatterns = [
    path('users/', views.UsersAPIView.as_view()),
    re_path('users/(?P<pk>\d+)/', views.UserAPIView.as_view(), name='user-detail'),
    re_path('users/action=(?P<action>[a-z]+)/',views.UsersAPIView.as_view())

]
