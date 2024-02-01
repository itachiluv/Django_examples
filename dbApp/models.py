from django.db import models

# Create your models here.
class person(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length = 20)
    empSalary = models.IntegerField()
    empAddress = models.CharField(max_length = 30)  
    

# def __str__(self):
#     return 'Employee shared details:'