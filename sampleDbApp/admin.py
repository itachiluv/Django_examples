from django.contrib import admin
from sampleDbApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    emp_list = ['fname','lname','city','pincode']

admin.site.register(Employee,EmployeeAdmin)