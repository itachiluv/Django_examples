from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_no = models.IntegerField()
    bus_name = models.CharField(max_length = 20)
    bus_from = models.CharField(max_length = 30)
    bus_destination = models.CharField(max_length = 30)
    
    # def __str__(self):
    #     return  f"{self.bus_name}"

class passanger(models.Model):
    pass_name = models.CharField(max_length = 20)
    pass_age = models.IntegerField()
    pass_from = models.CharField(max_length = 20)
    pass_destination = models.CharField(max_length = 20)
    