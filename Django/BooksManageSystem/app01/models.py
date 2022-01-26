from django.db import models

# Create your models here.

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46,null=False)
    address = models.CharField(max_length=64,null=False)
    # makemigrations migrate