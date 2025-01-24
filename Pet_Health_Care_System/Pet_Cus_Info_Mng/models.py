from django.db import models
from datetime import date
# Create your models here.
class Customer(models.Model):
    lastName = models.CharField(max_length=100, blank=False)
    firstName = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)  
    phoneNumber = models.CharField(max_length=15, blank=False)
    address = models.TextField(blank=False)
    age = models.PositiveIntegerField(blank=False)
    gender = models.CharField(
        max_length=10,
        choices=[("Nam", "Nam"), ("Nữ", "Nữ"), ("LGBT", "LGBT")],
        blank=False
    )
    def __str__(self):
        return f"{self.lastName} {self.firstName}"

class Pet(models.Model):
    id = models.AutoField(primary_key=True)  # ID
    name = models.CharField(max_length=100, blank=False)  # ten thu cung
    species = models.CharField(max_length=50, blank=False)  # giong loai (dog, cat, ...)
    gender = models.CharField(max_length=10, choices=[
        ("Đực", "Đực"), ("Cái", "Cái"),
    ], blank=False)  # gioi tinh
    dateOfBirth = models.DateField(null=True, blank=False)  # ngay sinh
    def calculatedAge(self):
        if self.dateOfBirth:
            today = date.today()
            age = today.year - self.dateOfBirth.year - (
                (today.month, today.day) < (self.dateOfBirth.month, self.dateOfBirth.day)
            )
            return age
        return None  # Trả về None nếu không có ngày sinh
    calculatedAge.short_description = "Age (calculated)"  # Đặt tên cột trong Admin
    age = models.IntegerField(null=True, blank=True)
    healthStatus = models.CharField(max_length=50, choices=[
        ('Đang nhập viện', 'Đang nhập viện'),
        ('Đang điều trị ngoại trú', 'Đang điều trị ngoại trú'),
        ('Đã xuất viện', 'Đã xuất viện'),
        ('Sức khỏe tốt','Sức khỏe tốt'),
        ('Cần tiêm phòng','Cần tiêm phòng'),
        ('Béo phì','Béo phì'),
        ('Bị chấn thương','Bị chấn thương'),
        ('Dinh dưỡng kém','Dinh dưỡng kém'),
        ('Giai đoạn cuối','Giai đoạn cuối'),
    ], blank=False)  # tinh trang suc khoe
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)  # Chu so huu
    def __str__(self):
        return f"{self.name} ({self.species})"
    # Tinh tuoi dua tren ngay sinh
    def calculate_age(self):
        if self.dateOfBirth:
            today = date.today()
            return today.year - self.dateOfBirth.year - (
                (today.month, today.day) < (self.dateOfBirth.month, self.dateOfBirth.day)
            )
        return None


class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medical_records', blank=False)
    date = models.DateField()
    treatmentDetails = models.TextField()
    doctor = models.CharField(max_length=255)
    remarks = models.TextField(blank=True)


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=50,
        choices=[('pending', 'Chưa thanh toán'), ('completed', 'Đã thanh toán')],
    )

    def __str__(self):
        return f"Appointment: {self.customer} - {self.pet} on {self.date} at {self.time}"

