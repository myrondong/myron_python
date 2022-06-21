from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from school import views

router = SimpleRouter()
router.register("students", views.StudentModelViewSet, basename="students")
urlpatterns = [
              ] + router.urls
