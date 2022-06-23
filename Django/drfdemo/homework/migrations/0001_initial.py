# Generated by Django 3.2.4 on 2022-06-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=18, verbose_name='课程名称')),
                ('description', models.TextField(default='暂无')),
                ('ontime', models.TimeField(verbose_name='上课时间')),
                ('outtime', models.TimeField(verbose_name='下课时间')),
                ('duration', models.DurationField(verbose_name='课时')),
                ('print', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
                'db_table': 'hk_course',
            },
        ),
    ]
