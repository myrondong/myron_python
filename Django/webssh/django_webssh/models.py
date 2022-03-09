from django.db import models


# Create your models here.

class LoginData(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=11)
    port = models.CharField(max_length=6)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = "login_data"  # 更改表名
