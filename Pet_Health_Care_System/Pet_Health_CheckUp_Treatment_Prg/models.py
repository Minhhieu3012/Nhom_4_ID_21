from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    health_status = models.CharField(max_length=100)

class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Mối quan hệ với Pet
    disease = models.CharField(max_length=200)  # Bệnh lý
    symptoms = models.CharField(max_length=200)  # Triệu chứng
    doctor = models.CharField(max_length=100)  # Bác sĩ điều trị
    consultation_date = models.DateField()  # Ngày khám
    notes = models.TextField(blank=True, null=True)  # Ghi chú thêm (tuỳ chọn)

    def __str__(self):
        return f'{self.pet.name} - {self.disease} - {self.consultation_date}'


class MedicalHistory(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Mối quan hệ với Pet
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)  # Mối quan hệ với Bệnh án
    date_of_treatment = models.DateField()  # Ngày điều trị
    doctor = models.CharField(max_length=100)  # Bác sĩ điều trị
    notes = models.TextField(blank=True, null=True)  # Ghi chú về quá trình điều trị

    def __str__(self):
        return f'{self.pet.name} - {self.record.disease} - {self.date_of_treatment}'
    

class Treatment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Mối quan hệ với Pet
    medication = models.CharField(max_length=200)  # Tên thuốc
    treatment_method = models.CharField(max_length=200)  # Phương pháp điều trị
    next_checkup_date = models.DateField()  # Ngày tái khám
    health_status_update = models.CharField(max_length=200, blank=True, null=True)  # Cập nhật tình trạng sức khỏe

    def __str__(self):
        return f'{self.pet.name} - {self.medication} - {self.next_checkup_date}'


class Medication(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Mối quan hệ với Pet
    medication_name = models.CharField(max_length=200)  # Tên thuốc
    dosage = models.CharField(max_length=100)  # Liều lượng
    frequency = models.CharField(max_length=100)  # Tần suất sử dụng
    start_date = models.DateField()  # Ngày bắt đầu sử dụng
    end_date = models.DateField()  # Ngày kết thúc sử dụng

    def __str__(self):
        return f'{self.pet.name} - {self.medication_name} - {self.start_date}'


class Notification(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Mối quan hệ với Pet
    message = models.TextField()  # Nội dung thông báo
    notification_date = models.DateField()  # Ngày gửi thông báo
    type = models.CharField(max_length=50, choices=[('reminder', 'Reminder'), ('alert', 'Alert')])  # Loại thông báo (nhắc nhở hoặc cảnh báo)

    def __str__(self):
        return f'{self.pet.name} - {self.type} - {self.notification_date}'

