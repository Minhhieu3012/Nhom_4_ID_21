# #------------------
# #Unit Testing
# #------------------
from django.test import TestCase
from datetime import date
from Pet_Health_CheckUp_Treatment_Prg.models import Pet, TreatmentProgress, MedicalRecord, Medication, Notification

class PetModelTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(
            name="Buddy",
            species="Chó",
            age=5,
            current_health_status="Khỏe mạnh"
        )

    def test_pet_str(self):
        # __str__ của Pet nên trả về tên của pet
        self.assertEqual(str(self.pet), "Buddy")


class MedicalRecordModelTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(
            name="Kitty",
            species="Mèo",
            age=3,
            current_health_status="Ốm"
        )
        self.medical_record = MedicalRecord.objects.create(
            pet=self.pet,
            date=date(2025, 2, 10),
            symptoms="Ốm và mệt mỏi",
            disease="Nhiễm trùng do virus",
            vet_notes="Cần được nghỉ ngơi và uống nhiều nước"
        )

    def test_medical_record_str(self):
        # __str__ trả về chuỗi: '<pet.name> - <date>'
        expected_str = f"{self.pet.name} - {self.medical_record.date}"
        self.assertEqual(str(self.medical_record), expected_str)


class TreatmentProgressModelTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(
            name="Charlie",
            species="Chó",
            age=4,
            current_health_status="Đang được điều trị"
        )
        self.medical_record = MedicalRecord.objects.create(
            pet=self.pet,
            date=date(2025, 2, 11),
            symptoms="Ho và hắt hơi",
            disease="Nhiễm trùng do vi khuẩn",
            vet_notes="Quản lý thuốc kháng sinh"
        )
        self.treatment_progress = TreatmentProgress.objects.create(
            pet=self.pet,
            medical_record=self.medical_record,
            treatment_method="Liệu pháp kháng sinh",
            next_appointment_date=date(2025, 2, 20),
            updated_health_status="Đang hồi phục"
        )
        # Nếu có thuốc liên quan, có thể thêm qua ManyToManyField
        self.medication = Medication.objects.create(
            name="Amoxicillin",
            description="Kháng sinh cho nhiễm trùng vi khuẩn",
            dosage_info="500mg/2 lần một ngày"
        )
        # Thêm thuốc cho tiến trình điều trị
        self.treatment_progress.medication.add(self.medication)

    def test_treatment_progress_str(self):
        # Kiểm tra __str__ có chứa tên thú cưng
        expected_start = f"Treatment for {self.pet.name} on "
        self.assertTrue(str(self.treatment_progress).startswith(expected_start))


class MedicationModelTest(TestCase):
    def setUp(self):
        self.medication = Medication.objects.create(
            name="Paracetamol",
            description="Thuốc giảm đau và hạ sốt",
            dosage_info="500mg/mỗi 6 tiếng"
        )

    def test_medication_str(self):
        self.assertEqual(str(self.medication), "Paracetamol")


class NotificationModelTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(
            name="Max",
            species="Chó",
            age=6,
            current_health_status="Khỏe mạnh"
        )
        self.notification = Notification.objects.create(
            pet=self.pet,
            message="Đã đến lúc tiêm vắc-xin hàng năm."
        )

    def test_notification_str(self):
        # Kiểm tra chuỗi trả về chứa tên của thú cưng và thông điệp
        notification_str = str(self.notification)
        self.assertIn(self.pet.name, notification_str)
        self.assertIn("Notification for", notification_str)
        