from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Mô hình cho vai trò của nhân viên (Role)
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Tên vai trò: ví dụ 'Bác sĩ thú y', 'Quản lý', 'Nhân viên'
    description = models.TextField(blank=True, null=True)  # Mô tả chi tiết về vai trò

    def __str__(self):
        return self.name

# Mô hình cho thông tin nhân viên (Staff)
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liên kết với tài khoản người dùng
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # Vai trò của nhân viên (ví dụ: Bác sĩ thú y)
    first_name = models.CharField(max_length=100)  # Tên nhân viên
    last_name = models.CharField(max_length=100)  # Họ nhân viên
    phone = models.CharField(max_length=15, blank=True, null=True)  # Số điện thoại
    email = models.EmailField(max_length=100, blank=True, null=True)  # Email liên lạc
    address = models.CharField(max_length=255, blank=True, null=True)  # Địa chỉ
    hire_date = models.DateField()  # Ngày tuyển dụng
    is_active = models.BooleanField(default=True)  # Trạng thái hoạt động (true: đang làm việc, false: nghỉ việc)
    date_of_birth = models.DateField(null=True, blank=True)  # Ngày sinh
    gender = models.CharField(max_length=10, choices=[('Male', 'Nam'), ('Female', 'Nữ'), ('Other', 'Khác')], blank=True, null=True)  # Giới tính
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)  # Số điện thoại liên lạc khẩn cấp
    profile_picture = models.ImageField(upload_to='staff_profile_pictures/', null=True, blank=True)  # Hình ảnh đại diện

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role.name}"

# Mô hình cho lịch làm việc của bác sĩ và nhân viên (WorkSchedule)
class WorkSchedule(models.Model):
    WORK_TYPES = [
        ('Consultation', 'Tư vấn'),
        ('Treatment', 'Điều trị'),
        ('Admin', 'Quản lý'),
        ('Other', 'Khác'),
    ]

    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    work_type = models.CharField(max_length=100, choices=WORK_TYPES)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_off_day = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def clean(self):
        """ Kiểm tra hợp lệ trước khi lưu dữ liệu """
        if self.start_time >= self.end_time:
            raise ValidationError("Thời gian kết thúc phải sau thời gian bắt đầu.")

    def save(self, *args, **kwargs):
        """ Gọi clean() trước khi lưu vào database """
        self.clean()
        super().save(*args, **kwargs)

# Mô hình quản lý quyền truy cập cho các nhân viên (UserPermission)
class UserPermission(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)  # Liên kết với nhân viên
    permission_type = models.CharField(
        max_length=50,
        choices=[('View', 'Xem'), ('Edit', 'Chỉnh sửa'), ('Delete', 'Xóa'), ('Admin', 'Quản trị')],
    )  # Loại quyền truy cập (Xem, Chỉnh sửa, Xóa, Quản trị)
    model_name = models.CharField(max_length=50)  # Tên mô hình (ví dụ: Pet, MedicalRecord, etc.)
    permission_description = models.TextField(blank=True, null=True)  # Mô tả quyền truy cập

    def __str__(self):
        return f"Permission {self.permission_type} for {self.staff.first_name} {self.staff.last_name} on {self.model_name}"

# Mô hình lưu trữ các loại ca làm việc của nhân viên (WorkShift)
class WorkShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)  # Liên kết với nhân viên
    shift_type = models.CharField(
        max_length=50,
        choices=[('Morning', 'Sáng'), ('Afternoon', 'Chiều'), ('Night', 'Tối')]
    )  # Ca làm việc (Sáng, Chiều, Tối)
    start_time = models.DateTimeField()  # Thời gian bắt đầu ca
    end_time = models.DateTimeField()  # Thời gian kết thúc ca
    is_active = models.BooleanField(default=True)  # Trạng thái ca làm việc (hoạt động hay không)

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} - {self.shift_type} shift"

