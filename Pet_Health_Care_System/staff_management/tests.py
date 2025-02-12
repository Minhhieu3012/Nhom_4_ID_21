from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from staff_management.models import Role, Staff, WorkSchedule

class WorkScheduleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser2", password="password")
        self.role = Role.objects.create(name="Nhân viên hỗ trợ", description="Hỗ trợ chăm sóc thú cưng")
        self.staff = Staff.objects.create(
            user=self.user,
            role=self.role,
            first_name="Trần",
            last_name="Văn C",
            phone="0123456789",
            email="staff2@example.com",
            hire_date="2024-01-15",
            is_active=True
        )

        # Chuyển datetime thành timezone-aware datetime
        start_time = timezone.make_aware(datetime(2025, 2, 12, 8, 0, 0))
        end_time = timezone.make_aware(datetime(2025, 2, 12, 12, 0, 0))

        self.schedule = WorkSchedule.objects.create(
            staff=self.staff,
            start_time=start_time,
            end_time=end_time,
            work_type="Consultation"
        )

    def test_schedule_creation(self):
        self.assertEqual(self.schedule.work_type, "Consultation")
        self.assertEqual(self.schedule.staff.first_name, "Trần")
