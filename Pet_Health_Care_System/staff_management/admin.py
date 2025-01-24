from django.contrib import admin
from .models import Staff, Schedule

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'role')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('staff', 'work_date', 'start_time', 'end_time')
    list_filter = ('work_date', 'staff')

