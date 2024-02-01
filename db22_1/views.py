from django.shortcuts import render
from .models import *
# Create your views here.
def get(request):
    allperson = Person.objects.all()
    print(allperson)
    person_dict={}
    return render(request,'db22_1/home1.html',context=person_dict)