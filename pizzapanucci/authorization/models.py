from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=128)
