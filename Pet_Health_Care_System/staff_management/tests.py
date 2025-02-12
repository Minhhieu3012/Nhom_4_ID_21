from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from staff_management.models import Role, Staff, WorkSchedule, UserPermission, WorkShift

class StaffManagementTests(TestCase):
    def setUp(self):
        """ Tạo dữ liệu mẫu cho các test cases """
        self.user = User.objects.create_user(username="testuser", password="password")
        self.role = Role.objects.create(name="Bác sĩ thú y", description="Chuyên điều trị thú cưng")
        
        self.staff = Staff.objects.create(
            user=self.user,
            role=self.role,
            first_name="Nguyễn",
            last_name="Văn A",
            phone="0987654321",
            email="test@example.com",
            hire_date="2023-01-15",
            is_active=True
        )

    def test_create_role_success(self):
        """ Kiểm tra tạo Role thành công """
        role = Role.objects.create(name="Quản lý", description="Quản lý nhân viên và hệ thống")
        self.assertEqual(role.name, "Quản lý")

    def test_create_staff_with_valid_data(self):
        """ Kiểm tra tạo Staff với thông tin đầy đủ """
        self.assertEqual(self.staff.first_name, "Nguyễn")
        self.assertEqual(self.staff.last_name, "Văn A")
        self.assertEqual(self.staff.role.name, "Bác sĩ thú y")
        self.assertTrue(self.staff.is_active)

    def test_create_staff_without_hire_date_fails(self):
        """ Kiểm tra không thể tạo Staff nếu thiếu hire_date """
        with self.assertRaises(IntegrityError):  # Django sẽ ném lỗi IntegrityError khi thiếu field bắt buộc
            Staff.objects.create(
                user=self.user,
                role=self.role,
                first_name="Trần",
                last_name="Văn B",
                phone="0123456789",
                email="staff2@example.com"
            )

    def test_work_schedule_start_before_end(self):
        """ Kiểm tra lịch làm việc không thể kết thúc trước khi bắt đầu """
        schedule = WorkSchedule(
            staff=self.staff,
            start_time=timezone.make_aware(datetime(2025, 2, 12, 12, 0, 0)),
            end_time=timezone.make_aware(datetime(2025, 2, 12, 8, 0, 0)),  # End < Start
            work_type="Consultation"
        )

        # Kiểm tra lỗi bằng cách chạy full_clean()
        with self.assertRaises(ValidationError):
            schedule.full_clean()  # Chạy validation trước khi lưu

    def test_valid_work_schedule_type(self):
        """ Kiểm tra WorkSchedule có thể lưu đúng work_type hợp lệ """
        schedule = WorkSchedule.objects.create(
            staff=self.staff,
            start_time=timezone.make_aware(datetime(2025, 2, 12, 8, 0, 0)),
            end_time=timezone.make_aware(datetime(2025, 2, 12, 12, 0, 0)),
            work_type="Consultation"
        )
        self.assertEqual(schedule.work_type, "Consultation")

    def test_invalid_work_schedule_type(self):
        """ Kiểm tra WorkSchedule không chấp nhận work_type không hợp lệ """
        schedule = WorkSchedule(
            staff=self.staff,
            start_time=timezone.make_aware(datetime(2025, 2, 12, 8, 0, 0)),
            end_time=timezone.make_aware(datetime(2025, 2, 12, 12, 0, 0)),
            work_type="InvalidType"  # Sai loại công việc
        )
        
        with self.assertRaises(ValidationError):
            schedule.full_clean()  # Chạy validation trước khi lưu

    def test_user_permission_assignment(self):
        """ Kiểm tra quyền truy cập được gán đúng cho nhân viên """
        permission = UserPermission.objects.create(
            staff=self.staff,
            permission_type="Edit",
            model_name="MedicalRecord",
            permission_description="Chỉnh sửa hồ sơ bệnh án"
        )
        self.assertEqual(permission.permission_type, "Edit")
        self.assertEqual(permission.model_name, "MedicalRecord")

    def test_create_work_shift(self):
        """ Kiểm tra ca làm việc với is_active=True """
        shift = WorkShift.objects.create(
            staff=self.staff,
            shift_type="Morning",
            start_time=timezone.make_aware(datetime(2025, 2, 12, 8, 0, 0)),
            end_time=timezone.make_aware(datetime(2025, 2, 12, 12, 0, 0)),
            is_active=True
        )
        self.assertTrue(shift.is_active)
