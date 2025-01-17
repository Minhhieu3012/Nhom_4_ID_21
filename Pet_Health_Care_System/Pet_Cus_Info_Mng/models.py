from django.db import models
from datetime import date
# Create your models here.
class Customer(models.Model):
    lastName = models.CharField(max_length=100, blank=False)
    firstName = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=255, blank=False)
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
    name = models.CharField(max_length=100)  # ten thu cung
    species = models.CharField(max_length=50)  # giong loai (dog, cat, ...)
    gender = models.CharField(max_length=10, choices=[
        ("Male", "Đực"), ("Female", "Cái"),
    ])  # gioi tinh
    date_of_birth = models.DateField()  # ngay sinh
    age = models.IntegerField(null=True, blank=True)
    health_status = models.CharField(max_length=50, choices=[
        ('hospitalized', 'Đang nhập viện'),
        ('outpatient', 'Đang điều trị ngoại trú'),
        ('discharged', 'Đã xuất viện')
    ])  # tinh trang suc khoe
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Chu so huu

    def __str__(self):
        return f"{self.name} ({self.species})"
     # Tinh tuoi dua tren ngay sinh
    def calculate_age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None


class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medical_records')
    date = models.DateField()
    treatment_details = models.TextField()
    doctor = models.CharField(max_length=255)
    remarks = models.TextField(blank=True)


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Đang chờ xử lý'), ('completed', 'Đã hoàn thành xong')])
