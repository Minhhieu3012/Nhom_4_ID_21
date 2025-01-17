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
    room_type = models.CharField(max_length=20)
    capacity = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Under Maintenance', 'Under Maintenance')],
        default='Available'
    )

class Admission(models.Model):
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)  # Thú cưng nhập viện
    room = models.ForeignKey('Room', on_delete=models.CASCADE)  # Chuồng/phòng được chỉ định
    admission_date = models.DateTimeField(default=now)  # Ngày nhập viện
    discharge_date = models.DateTimeField(null=True, blank=True)  # Ngày xuất viện (có thể để trống)

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

    def __str__(self):
        return f"Invoice #{self.id} - Admission #{self.admission.id}"

    def calculate_total(self):
        """
        Tính tổng số tiền dựa trên các dịch vụ liên quan và thời gian nằm viện.
        """
        days_hospitalized = (self.admission.discharge_date - self.admission.admission_date).days if self.admission.discharge_date else 1
        room_cost = days_hospitalized * self.admission.room.daily_rate
        service_cost = sum(service.cost for service in self.admission.service_set.all())  # Dịch vụ liên quan
        self.total_amount = room_cost + service_cost
        self.save()