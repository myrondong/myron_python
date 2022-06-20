from django.contrib import admin
from django.urls import path, include, re_path
from . import views

# rest_framework.routers 使用方法
urlpatterns = [

    # APiViwe
    path("students/", views.StudentApiView.as_view()),
    # re_path 就是path 上可以使用正则表达式
    re_path("^students/(?P<pk>[0-9]+)/$", views.StudentInfoApiView.as_view()),

    # GenericAPIView
    path("studentsg/", views.StudentGenericAPIView.as_view()),
    re_path("^studentsg/(?P<pk>[0-9]+)/$", views.StudentInfoGenericAPIView.as_view()),

    # mixins+GenericAPIView
    path("studentsm/", views.StudentMixinsAPIView.as_view()),
    re_path("^studentsm/(?P<pk>[0-9]+)/$", views.StudentInfoMixinsAPIView.as_view()),
    # 试图子类
    path("studentsson/", views.StudentView.as_view()),
    re_path("^studentsson/(?P<pk>[0-9]+)/$", views.StudentInfoView.as_view()),

    # ViewSet
    # path("studentset/", views.StudentViewSet.as_view({"http请求动作":"视图方法"})),
    path("studentset/",views.StudentViewSet.as_view(
        {
            "get":"get_list",
            "post":"create_student",
        })),

    re_path("^studentset/(?P<pk>[0-9]+)/$", views.StudentViewSet.as_view(
        {
            "get": "get_one_sutdent",
            "put":"update_student",
            "delete":"delet_one_student",
         })),

    # GenericViewSet
    # path("studentset/", views.StudentViewSet.as_view({"http请求动作":"视图方法"})),
    path("studentgset/",views.StudentGenericViewSet.as_view(
        {
            "get":"get_student_list",
            "post":"create",

        })),

    re_path("^studentgset/(?P<pk>[0-9]+)/$", views.StudentGenericViewSet.as_view(
        {
            "get": "retrieve",
            "put":"update",
            "delete":"delete_student",
         })),
    # MixinsViewSet
    path("studentgsetminx/", views.StudentMixinsViewSet.as_view(
        {
            "get": "list",
            "post": "create",

        })),

    re_path("^studentgsetminx/(?P<pk>[0-9]+)/$", views.StudentMixinsViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "delete": "destroy",
        })),

    # ReadOnlyModelViewSet
    path("studentgsetReadOnly/", views.StudentReadOnlyModelViewSet.as_view(
        {
            "get": "list",
            "post": "create",

        })),

    re_path("^studentgsetReadOnly/(?P<pk>[0-9]+)/$", views.StudentReadOnlyModelViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "delete": "destroy",
        })),

    # # ModelViewSet
    # path("studentgsetModelViewSet/", views.StudentModelViewSet.as_view(
    #     {
    #         "get": "list",
    #         "post": "create",
    #
    #     })),
    #
    # re_path("^studentgsetModelViewSet/(?P<pk>[0-9]+)/$", views.StudentModelViewSet.as_view(
    #     {
    #         "get": "retrieve",
    #         "put": "update",
    #         "delete": "destroy",
    #     })),

]

# 自动生成路由+这个和视图集一起使用的
from rest_framework.routers import DefaultRouter,SimpleRouter
# 1、实例化类
router=DefaultRouter()
# 2、注册视图集
# 这里面不可以用正则
router.register("studentgsetModelViewSet",views.StudentModelViewSet,basename="studentgsetModelViewSet")
# 3、把生成的路由列表，和urlpatterns进行拼接
print(router.urls)
urlpatterns+=router.urls

