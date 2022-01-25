from django.contrib import admin
from django.urls import path, include
from myadmin.views import index
from myadmin.views import user
# 后台管理子路由
urlpatterns = [
    # 后台首页路由
    path('', index.index, name='myadmin_index'),

    # 员工信息管理路由
    path('user/<int:p_index>', user.index, name='myadmin_user_index'),
    path('user/add', user.add, name='myadmin_user_add'),
    path('user/insert', user.insert, name='myadmin_user_insert'),
    path('user/edit<int:uid>', user.edit, name='myadmin_user_edit'),
    path('user/del<int:uid>', user.delete, name='myadmin_user_delete'),
    path('user/update<int:uid>', user.update, name='myadmin_user_update'),

]
