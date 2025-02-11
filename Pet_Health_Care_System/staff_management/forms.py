from django import forms
from .models import Staff, WorkSchedule, WorkShift


# --- Staff Form ---
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'role', 'first_name', 'last_name', 'phone', 'email', 'address', 'hire_date', 'is_active', 'date_of_birth', 'gender', 'emergency_contact', 'profile_picture']

# --- WorkSchedule Form ---
class WorkScheduleForm(forms.ModelForm):
    class Meta:
        model = WorkSchedule
        fields = ['staff', 'start_time', 'end_time', 'work_type', 'location', 'is_off_day', 'notes']

# --- WorkShift Form ---
class WorkShiftForm(forms.ModelForm):
    class Meta:
        model = WorkShift
        fields = ['staff', 'shift_type', 'start_time', 'end_time', 'is_active']
