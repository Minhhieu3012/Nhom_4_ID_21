from django.contrib import admin
from .models import Role, Staff, WorkingSchedule, Appointment, AuditLog, Notification

# Đăng ký các mô hình vào Django Admin
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'can_manage_schedule', 'can_view_appointments', 'can_edit_pet_info', 'can_manage_users')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'phone_number', 'email', 'join_date', 'is_active')
    search_fields = ('full_name', 'email')
    list_filter = ('role', 'is_active')

@admin.register(WorkingSchedule)
class WorkingScheduleAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'start_time', 'end_time', 'is_off_day', 'is_overtime')
    list_filter = ('date', 'is_off_day', 'is_overtime')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'pet_name', 'pet_type', 'doctor', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('appointment_date', 'status')

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')
    list_filter = ('timestamp',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('staff', 'message', 'is_read', 'timestamp')
    list_filter = ('is_read', 'timestamp')
