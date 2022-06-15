from django.db import models


class UserModel(models.Model):
    employee_number = models.CharField(max_length=9, unique=True, verbose_name="员工号")  # 用户名唯一

    password = models.CharField(max_length=256, verbose_name="密码")

    name = models.CharField(max_length=25, verbose_name="用户姓名")

    user_level = models.IntegerField(default=2, verbose_name="用户等级")

    email = models.EmailField(verbose_name="邮箱",null=True)

    phone = models.CharField(max_length=11, verbose_name="手机号码",null=True)

    class Meta:
        db_table = 'user'
