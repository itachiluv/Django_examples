from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name


class DailyTask(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    date = models.DateField()
    task = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.trainee.name}'s Task on {self.date}"


class admin_mine(models.Model):
    name = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name
