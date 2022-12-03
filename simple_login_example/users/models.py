from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True) #unique 중복 막기
    password = models.CharField(max_length=50)