from django.db import models

class Staff(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Bác sĩ thú y'),
        ('assistant', 'Trợ lý'),
        ('receptionist', 'Lễ tân'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=128)  # Hash mật khẩu

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='schedules')
    work_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} - {self.work_date}"
