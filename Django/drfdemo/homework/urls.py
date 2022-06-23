
from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('hk/',views.CourseAPIView.as_view()),
    re_path('^hk/(?P<pk>\d+)/$', views.CourseInfoAPIView.as_view()),
]
