from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Appointment(models.Model):
    datetime = models.DateTimeField()
    pet = models.ForeignKey('Pets', on_delete=models.CASCADE, related_name='appointments')
    service_type = models.CharField(max_length=100, choices=[
        ('checkup', 'Check-up'),
        ('vaccination', 'Vaccination'),
        ('grooming', 'Grooming'),
        ('surgery', 'Surgery'),
    ])
    vet = models.ForeignKey('Vet', on_delete=models.CASCADE, related_name='appointments')

    def cancel(self):
        self.delete()

    def schedule(self):
        self.save()

    def __str__(self):
        pet_name = self.pet.name if self.pet else "Unknown Pet"
        vet_name = self.vet.name if self.vet else "Unknown Vet"
        return f"Appointment for {self.pet.name} ({self.service_type}) with {self.vet.name} on {self.datetime}"

class Vet(models.Model):
    contact_info = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Customers(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class Pets(models.Model):
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


