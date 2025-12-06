from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    auther=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    Created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Task(models.Model):
    pass