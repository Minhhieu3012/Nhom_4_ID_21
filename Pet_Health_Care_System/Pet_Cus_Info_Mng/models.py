from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)  # ID tu dong tang
    name = models.CharField(max_length=255)  # Ten khach hang
    phone_number = models.CharField(max_length=20) 
    address = models.TextField()  # Địa chỉ
    gender = models.CharField(max_length=10, choices=[
        ("Male", "Nam"), ("Female", "Nữ"),
    ])  # gioi tinh

    def __str__(self):
        return self.name


class Pet(models.Model):
    id = models.AutoField(primary_key=True)  # ID
    name = models.CharField(max_length=100)  # ten thu cung
    species = models.CharField(max_length=50)  # giong loai (dog, cat, ...)
    gender = models.CharField(max_length=10, choices=[
        ("Male", "Đực"), ("Female", "Cái"),
    ])  # gioi tinh
    date_of_birth = models.DateField()  # ngay sinh
    age = models.IntegerField()  # tuoi (tinh tu dong or nhap thu cong)
    health_status = models.CharField(max_length=50, choices=[
        ("Healthy", "Khỏe mạnh"), ("Sick", "Đang bệnh"), ("Recovering", "Đang hồi phục"),
    ])  # tinh trang suc khoe
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Chu so huu

    def __str__(self):
        return f"{self.name} ({self.species})"

