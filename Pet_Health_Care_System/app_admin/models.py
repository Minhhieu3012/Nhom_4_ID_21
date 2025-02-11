from django.db import models
from django.utils.timezone import now

# Create your models here.
GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
]
class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=20)
    breed = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    birth_day = models.DateField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)  # Liên kết với chủ thú cưng
    def __str__(self):
        return f"{self.name} ({self.species})"
class Owner(models.Model):
    full_name = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=12)
    email = models.CharField (max_length=50)
    address = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    def __str__(self):
        return self.full_name

class Room(models.Model):
    room_type = models.CharField(
        max_length=20,
        choices=[
            ('Standard', 'Standard'),
            ('Luxury', 'Luxury'),
            ('Indoor', 'Indoor'),
            ('Outdoor', 'Outdoor'),
            ('Quarantine', 'Quarantine'),
            ('Recovery', 'Recovery'),
            ('Training', 'Training'),
            ('Breeding', 'Breeding'),
            ('Large', 'Large Animal'),
            ('Custom', 'Customizable'),
        ],
        default='Standard'
    )
    capacity = models.IntegerField()
    current_occupancy = models.IntegerField(default=0) 
    status = models.CharField(
        max_length=20,
        choices=[('Available', 'Available'),
                ('Occupied', 'Occupied'), 
                ('Under Maintenance', 'Under Maintenance')],
        default='Available'
    )
    def update_status(self):
    #"""Cập nhật trạng thái phòng dựa trên số lượng thú"""
        if self.current_occupancy >= self.capacity:
            self.status = 'Occupied'
        else:
            self.status = 'Available'
        self.save()  # Đảm bảo lưu lại thay đổi

    def __str__(self):
        return f"{self.room_type} - {self.status}"

class Admission(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    admission_date = models.DateTimeField( default=now)
    discharge_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Admission for {self.pet.name} on {self.admission_date.strftime('%Y-%m-%d')}"
    
class Staff(models.Model):
    full_name = models.CharField(max_length=100) 
    role = models.CharField(
        max_length=20,
        choices=[('Veterinarian', 'Veterinarian'), ('Caretaker', 'Caretaker'), ('Admin', 'Admin')],
        default='Caretaker'
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)  
    email = models.EmailField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    def __str__(self):
        return f"{self.full_name} - {self.role}"
    


class Invoice(models.Model):
    admission = models.ForeignKey('Admission', on_delete=models.CASCADE)  # Liên kết với thông tin nhập viện
    issued_date = models.DateTimeField(default=now)  # Ngày hóa đơn được phát hành
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Tổng số tiền
    is_paid = models.BooleanField(default=False)  # Trạng thái thanh toán (Đã thanh toán hay chưa)
    payment_date = models.DateTimeField(null=True, blank=True)  # Ngày thanh toán (nếu đã thanh toán)
    notes = models.TextField(null=True, blank=True)  # Ghi chú (nếu có)

    
    def calculate_total(self):
        if self.admission.discharge_date and self.admission.admission_date:
            days_hospitalized = max((self.admission.discharge_date - self.admission.admission_date).days, 1)
        else:
            days_hospitalized = 1

        room_prices = {
            "Standard": 50,
            "Luxury": 100,
            "Indoor": 70,
            "Outdoor": 60,
            "Quarantine": 80,
            "Recovery": 90,
            "Training": 75,
            "Breeding": 85,
            "Large": 120,
            "Custom": 110,
        }
        
        room_cost = room_prices.get(self.admission.room.room_type, 50) * days_hospitalized

        # Nếu không có service, chỉ tính tiền phòng
        self.total_amount = room_cost
        self.save()
