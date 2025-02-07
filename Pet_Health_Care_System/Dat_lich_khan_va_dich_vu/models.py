import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Appointment(models.Model):
    AppointmentID = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    pet = models.ForeignKey('Pets', on_delete=models.CASCADE, related_name='appointments', db_column="PetID")
    vet = models.ForeignKey('Vet', on_delete=models.CASCADE, related_name='appointments', db_column="VetID")
    service_type = models.CharField(max_length=100, choices=[
        ('checkup', 'Check-up'),
        ('vaccination', 'Vaccination'),
        ('grooming', 'Grooming'),
        ('surgery', 'Surgery'),
    ])
    def cancel_appointment(self):
        self.delete()

    def schedule(self):
        self.save()

    def GetDetails(self):
        return {
            "AppointmentID": self.AppointmentID,
            "pet": self.pet.name,
            "vet": self.vet.name,
            "datetime": self.datetime,
            "service_type": self.service_type,
        }

    def UpdateDetails(self, datetime=None, service_type=None, vet=None):
        if datetime:
            self.datetime = datetime
        if service_type:
            self.service_type = service_type
        if vet:
            self.vet = vet
        self.save()

    def __str__(self):
        return f"Appointment {self.AppointmentID} for {self.pet.name} ({self.service_type}) with {self.vet.name} on {self.datetime}"

class Vet(models.Model):
    VetID = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100, default="N/A")

    def GetDetails(self):
        return {
            "VetID": self.VetID,
            "name": self.name,
            "contact_info": self.contact_info,
        }

    def UpdateDetails(self, name=None, contact_info=None):
        if name:
            self.name = name
        if contact_info:
            self.contact_info = contact_info
        self.save()

    def __str__(self):
        return self.name

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Customers(AbstractBaseUser, PermissionsMixin):
    CustomerID = models.CharField(max_length=50, unique=True, default=uuid.uuid4)  
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def update_profile(self, email=None, phone=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        self.save()

    def GetDetails(self):
        return {
            "CustomerID": self.CustomerID,
            "email": self.email,
            "phone": self.phone,
        }

    def UpdateDetails(self, email=None, phone=None):
        self.update_profile(email, phone)

    def __str__(self):
        return self.email

class Pets(models.Model):
    PetID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='pets', null=True, blank=True)
    age = models.IntegerField()
    health_record = models.TextField()
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.species})"

class Payment(models.Model):
    amount = models.FloatField()
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('refunded', 'Refunded'),
    ])

    def process_payment(self):
        self.status = 'completed'
        self.save()

    def refund_payment(self):
        self.status = 'refunded'
        self.save()

    def __str__(self):
        return f"Payment of {self.amount} by {self.customer.email} on {self.payment_date}"
