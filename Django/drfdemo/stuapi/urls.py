from django.urls import path,re_path
from . import views
urlpatterns = [
    path('students/', views.StudentsView.as_view()),
    re_path('^students/(?P<pk>\d+)/$', views.StudentInfo.as_view()),

]
