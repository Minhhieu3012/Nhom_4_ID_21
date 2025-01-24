from django.db import models

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
        return f"Appointment for {self.pet.name} ({self.service_type}) with {self.vet.name} on {self.datetime}"

class Vet(models.Model):
    contact_info = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pets(models.Model):
    age = models.IntegerField()
    health_record = models.TextField()
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.species})"

class Customers(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.email

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

