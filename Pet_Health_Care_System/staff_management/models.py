from django.db import models
from django.contrib.auth.models import User

# Mô hình phân quyền
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Tên vai trò
    description = models.TextField()  # Mô tả quyền hạn
    can_manage_schedule = models.BooleanField(default=False)  # Quyền quản lý lịch làm việc
    can_view_appointments = models.BooleanField(default=False)  # Quyền xem lịch hẹn
    can_edit_pet_info = models.BooleanField(default=False)  # Quyền chỉnh sửa thông tin thú cưng
    can_manage_users = models.BooleanField(default=False)  # Quyền quản lý người dùng

    def __str__(self):
        return self.name

# Mô hình nhân viên
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    join_date = models.DateField(auto_now_add=True)  # Ngày gia nhập
    is_active = models.BooleanField(default=True)  # Trạng thái làm việc (active/inactive)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Ảnh đại diện

    def __str__(self):
        return self.full_name

# Mô hình lịch làm việc
class WorkingSchedule(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_off_day = models.BooleanField(default=False)  # Ngày nghỉ
    is_overtime = models.BooleanField(default=False)  # Làm ngoài giờ

    def __str__(self):
        return f'{self.staff.full_name} - {self.date}'

    def is_available(self):
        # Kiểm tra xem bác sĩ có sẵn trong khoảng thời gian này không
        return not self.is_off_day and not self.is_overtime

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
    )  # Trạng thái của lịch hẹn
    notes = models.TextField(null=True, blank=True)  # Ghi chú về lịch hẹn

    def __str__(self):
        return f'{self.customer_name} - {self.pet_name} ({self.appointment_date} {self.appointment_time})'

# Mô hình lịch sử hoạt động
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # Mô tả hành động (ví dụ: "Đã thêm bác sĩ", "Đã xóa lịch hẹn")
    timestamp = models.DateTimeField(auto_now_add=True)  # Thời gian thực hiện hành động

    def __str__(self):
        return f'{self.user.username} - {self.action} - {self.timestamp}'

# Mô hình thông báo
class Notification(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()  # Nội dung thông báo
    is_read = models.BooleanField(default=False)  # Trạng thái đọc chưa
    timestamp = models.DateTimeField(auto_now_add=True)  # Thời gian thông báo

    def __str__(self):
        return f'Thông báo cho {self.staff.full_name} - {self.timestamp}'
