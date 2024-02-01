# trainee_details/forms.py

from django import forms
from .models import Trainee, DailyTask


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ["name", "email"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = DailyTask
        fields = ["date", "task", "completed"]
