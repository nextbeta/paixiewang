from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, verbose_name="账户名");
    pwd = models.CharField(max_length=100, verbose_name="密码");
    icon = models.CharField(max_length=40, default=' ');
    token = models.CharField(max_length=256, default=' ');