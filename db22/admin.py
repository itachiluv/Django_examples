from django.contrib import admin
from db22.models import Bus, passanger
# Register your models here.
class BusAdmin(admin.ModelAdmin):
    list_display = ['bus_no','bus_name','bus_from','bus_destination']
    
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['pass_name','pass_age','pass_from','pass_destination']

admin.site.register(Bus, BusAdmin)
admin.site.register(passanger, PassengerAdmin)

