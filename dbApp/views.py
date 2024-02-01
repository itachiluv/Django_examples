from django.shortcuts import render
from dbApp.models import person
# Create your views here.

def personDetails(request):
    per_data = person.objects.all()
    person_dict = {'person_list':per_data}
    return render(request,'personApp/person.html',context=person_dict)