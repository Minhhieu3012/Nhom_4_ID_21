from django import forms
from .models import Staff, WorkingSchedule

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'role', 'full_name', 'phone_number', 'email', 'is_active', 'profile_picture']

class WorkingScheduleForm(forms.ModelForm):
    class Meta:
        model = WorkingSchedule
        fields = ['staff', 'date', 'start_time', 'end_time', 'is_off_day', 'is_overtime']
