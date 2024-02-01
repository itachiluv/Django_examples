from django.contrib import admin
from trainee.models import Trainee, DailyTask, admin_mine

admin.site.register(Trainee)
admin.site.register(DailyTask)
admin.site.register(admin_mine)
