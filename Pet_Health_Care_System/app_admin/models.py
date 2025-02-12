from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Quản trị viên'),
        ('doctor', 'Bác sĩ thú y'),
        ('staff', 'Nhân viên'),
        ('customer', 'Khách hàng'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

# Create your models here.
