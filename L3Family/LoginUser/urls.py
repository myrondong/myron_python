from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('reg', RegList, 'reg')
router.register('log', LogList, 'log')
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api/', include_docs_urls()),
]
