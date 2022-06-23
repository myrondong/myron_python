from django.db import models
from datetime import datetime
# Create your models here.

class HomeWork(models.Model):
    name = models.CharField(max_length=18,verbose_name="课程名称",db_index=True)
    description = models.TextField(default='暂无')
    ontime = models.TimeField(verbose_name='上课时间')
    outtime = models.TimeField(verbose_name='下课时间')
    duration = models.DurationField(verbose_name='课时')
    print = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='价格')

    class Meta:
        db_table = 'hk_course'
        verbose_name='课程信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name