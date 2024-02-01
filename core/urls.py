"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as v1
from timeApp import views as v2
from dbApp import views as v3
from sampleDbApp import views as v4
from db22 import views as v5
from db22_1 import views as v6
from logApp import views as v7
from trainee import views as t

urlpatterns = [
    path("", v1.home, name="index"),
    path("admin/", admin.site.urls),
    path("page2", v1.index2),
    path("time/", v2.time_date),
    path("template/", v1.temp_dis),
    path("temp_date/", v2.time_temp),
    path("personData/", v3.personDetails),
    path("employee/", v4.emp_details),
    path("bus/", v5.bus_details),
    path("get/", v6.get),
    path("set_session/", v5.set_session),
    path("get_session/", v5.get_session),
    path("login/", v7.user_login),
    path("logout/", v7.user_logout),
    path("json_data/", v5.json_data),
    path("trainee/", t.index, name="trainee_home"),
    path("update/<int:trainee_id>", t.update_trainee),
    path(
        "view_details/<int:trainee_id>",
        t.view_trainee_details,
        name="view_trainee_details",
    ),
    path("add_task/<int:trainee_id>/", t.add_task, name="add_task"),
    path("login/", t.admin_login, name="login"),
    path("logout/", t.admin_logout, name="admin_logout"),
]
