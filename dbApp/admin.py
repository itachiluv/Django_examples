from django.contrib import admin
from dbApp.models import person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    emp_details = ['empNo','empName','empSalary','empAddress']

admin.site.register(person,PersonAdmin)