from django.shortcuts import render
from sampleDbApp.models import Employee
# Create your views here.
def emp_details(request):
    emp_data = Employee.objects.all()
    emp_dict = {'employee_detail': emp_data}
    return render(request,'sampleDbApp/employee.html',context=emp_dict)