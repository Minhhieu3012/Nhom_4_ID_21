from django.contrib import admin
from .models import Role, Staff, WorkSchedule, UserPermission, WorkShift

# --- Role Admin ---
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Role, RoleAdmin)

# --- Staff Admin ---
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'email', 'phone', 'hire_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('role', 'is_active')

admin.site.register(Staff, StaffAdmin)

# --- WorkSchedule Admin ---
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('staff', 'start_time', 'end_time', 'work_type', 'location', 'is_off_day')
    list_filter = ('staff', 'work_type', 'is_off_day')
    search_fields = ('staff__first_name', 'staff__last_name', 'work_type')

admin.site.register(WorkSchedule, WorkScheduleAdmin)

# --- UserPermission Admin ---
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('staff', 'permission_type', 'model_name', 'permission_description')
    list_filter = ('permission_type', 'model_name')
    search_fields = ('staff__first_name', 'staff__last_name', 'model_name')

admin.site.register(UserPermission, UserPermissionAdmin)

# --- WorkShift Admin ---
class WorkShiftAdmin(admin.ModelAdmin):
    list_display = ('staff', 'shift_type', 'start_time', 'end_time', 'is_active')
    list_filter = ('shift_type', 'is_active')
    search_fields = ('staff__first_name', 'staff__last_name', 'shift_type')

admin.site.register(WorkShift, WorkShiftAdmin)
