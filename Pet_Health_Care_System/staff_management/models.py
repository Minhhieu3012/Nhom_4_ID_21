from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import timedelta

# Mô hình phân quyền
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Tên vai trò
    description = models.TextField()  # Mô tả quyền hạn
    can_manage_schedule = models.BooleanField(default=False)  # Quản lý lịch làm việc
    can_view_appointments = models.BooleanField(default=False)  # Xem lịch hẹn
    can_edit_pet_info = models.BooleanField(default=False)  # Chỉnh sửa thông tin thú cưng
    can_manage_users = models.BooleanField(default=False)  # Quản lý người dùng
    can_manage_doctor_schedule = models.BooleanField(default=False)  # Quản lý lịch bác sĩ
    can_confirm_appointments = models.BooleanField(default=False)  # Xác nhận/hủy lịch hẹn
    can_view_reports = models.BooleanField(default=False)  # Truy cập báo cáo & thống kê

    def __str__(self):
        return self.name

# Mô hình nhân viên
class Staff(models.Model):
    WORK_STATUS_CHOICES = [
        ('working', 'Đang làm việc'),
        ('on_break', 'Nghỉ giải lao'),
        ('off_duty', 'Hết ca làm'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    work_status = models.CharField(max_length=20, choices=WORK_STATUS_CHOICES, default='working')

    def __str__(self):
        return self.full_name

    def get_appointment_count(self):
        return Appointment.objects.filter(doctor=self).count()
    
    def get_total_work_hours(self):
        schedules = WorkingSchedule.objects.filter(staff=self)
        total_hours = sum((schedule.end_time.hour - schedule.start_time.hour) for schedule in schedules)
        return total_hours

# Mô hình lịch làm việc
class WorkingSchedule(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_off_day = models.BooleanField(default=False)
    is_overtime = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.staff.full_name} - {self.date}'

    def is_available(self):
        return not self.is_off_day and not self.is_overtime

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Thời gian bắt đầu phải nhỏ hơn thời gian kết thúc.")

        overlapping_schedules = WorkingSchedule.objects.filter(
            staff=self.staff,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(pk=self.pk)

        if overlapping_schedules.exists():
            raise ValidationError("Lịch làm việc bị trùng lặp.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

# Mô hình lịch hẹn
class Appointment(models.Model):
    customer_name = models.CharField(max_length=255)
    pet_name = models.CharField(max_length=255)
    pet_type = models.CharField(max_length=100)
    doctor = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, limit_choices_to={'role__name': 'Bác sĩ thú y'})
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(
        max_length=50,
        choices=[('pending', 'Chưa xác nhận'), ('confirmed', 'Đã xác nhận'), ('canceled', 'Đã hủy')],
        default='pending'
    )
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer_name} - {self.pet_name} ({self.appointment_date} {self.appointment_time})'

    def save(self, *args, **kwargs):
        action = 'created' if self._state.adding else 'updated'
        super().save(*args, **kwargs)
        AppointmentHistory.objects.create(appointment=self, user=self.doctor.user, action=action)
        Notification.objects.create(
            staff=self.doctor,
            message=f"Lịch hẹn mới: {self.customer_name} - {self.pet_name} vào {self.appointment_date} {self.appointment_time}"
        )

# Mô hình lịch sử hoạt động của lịch hẹn
class AppointmentHistory(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50, choices=[
        ('created', 'Tạo mới'),
        ('updated', 'Cập nhật'),
        ('canceled', 'Hủy lịch'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.action} {self.appointment}'

# Mô hình lịch sử hoạt động chung
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action} - {self.timestamp}'

# Mô hình thông báo
class Notification(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Thông báo cho {self.staff.full_name} - {self.timestamp}'
