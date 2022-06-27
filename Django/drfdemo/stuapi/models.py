from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25,verbose_name='姓名',help_text="xingming")
    sex = models.BooleanField(default=1,verbose_name='性别',help_text='nan nv')
    age =models.IntegerField(verbose_name='年龄',help_text='年龄不能小于0')
    classmate = models.CharField(max_length=5,verbose_name="班级编号")
    description =models.TextField(max_length=1000,verbose_name='个性签名')
    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生'
        verbose_name_plural=verbose_name