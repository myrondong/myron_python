# Generated by Django 2.1.2 on 2022-01-24 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=46)),
                ('address', models.CharField(max_length=64)),
            ],
        ),
    ]
