from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    tel = models.CharField(max_length=11)
    employee_num = models.CharField(max_length=7)

    class Meta:
        db_table = 'user'
