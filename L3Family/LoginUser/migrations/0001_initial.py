# Generated by Django 3.2.4 on 2022-06-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=9, unique=True, verbose_name='员工号')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('name', models.CharField(max_length=25, verbose_name='用户姓名')),
                ('user_level', models.IntegerField(default=2, verbose_name='用户等级')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
            ],
        ),
    ]
