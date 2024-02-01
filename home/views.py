from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    user = [
        {"name": "Messi", "Age": 24},
        {"name": "Mani", "Age": 2},
        {"name": "Ronadlo", "Age": 36},
        {"name": "Neymar", "Age": 25},
        {"name": "Luffy", "Age": 19},
    ]
    return render(request, "index.html", context={"user_send": user})


def index2(request):
    player = ["Messi", "Mani", "Ronaldo", "Neymar"]
    return render(request, "page2.html", context={"player_name": player})


def temp_dis(request):
    return render(request, "homeApp/timeApp_dis.html")
