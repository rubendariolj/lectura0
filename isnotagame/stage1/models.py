from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    accomplishment = models.CharField(null=True, max_length=64)
    date = models.DateField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.time}"

class Category(models.Model):
    categories = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.categories}"

class Questions(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    question = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=64)
    answer2 = models.CharField(max_length=64)
    answer3 = models.CharField(max_length=64)
    answer4 = models.CharField(max_length=64)
    correctanswerchar =  models.CharField(max_length=64)
    correctanswerint =  models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.pk}"

class Stages(models.Model):
    stage = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=500)
    userstat = models.ManyToManyField(User, blank=True, related_name="stages")

    def __str__(self):
        return f"{self.stage}"