from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from db22.models import Bus, passanger
import json

# Create your views here.


def bus_details(request):
    bus_all = Bus.objects.all()
    pass_all = passanger.objects.all()
    bus_dict = {"bus_list": bus_all}
    pass_dict = {"pass_list": pass_all}
    return render(
        request,
        "busApp/bus.html",
        context={"bus_dict": bus_dict, "pass_dict": pass_dict},
    )


def json_data(request):
    bus_all = Bus.objects.all()
    json_data = serialize("json", bus_all)
    # print(json_data)
    json_data = json.loads(json_data)

    # Dump the data back to a formatted JSON string
    formatted_json_string = json.dumps(json_data, indent=2)
    print(formatted_json_string)
    return JsonResponse(formatted_json_string, safe=False)


json_send_data = json_data
# views.py
# from django.shortcuts import render


def set_session(request):
    request.session["favorite_color"] = "test"
    return render(request, "busApp/bus.html")


def get_session(request):
    favorite_color = request.session.get("favorite_color", "test")
    return render(request, "busApp/bus.html", {"favorite_color": favorite_color})


# views.py
def clear_session(request):
    request.session.pop("favorite_color", None)
    return render(request, "busApp/bus.html")


# views.py
def clear_all_sessions(request):
    request.session.clear()
    return render(request, "busApp/bus.html")
