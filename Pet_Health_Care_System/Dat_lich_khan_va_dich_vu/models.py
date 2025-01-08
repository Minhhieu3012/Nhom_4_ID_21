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
    # def __str__(self):
        #return f"Appointment {self.id} for {self.pet.name} with {self.vet.name} on {self.datetime.strftime('%Y-%m-%d %H:%M')}"



class Vet(models.Model):
    contact_info = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def update_record(self):
        # Logic to update records
        pass

    def view_appointments(self):
        return self.appointments.all()
    


class Pets(models.Model):
    age = models.IntegerField()
    health_record = models.TextField()
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)

    def get_details(self):
        return f"{self.name}, {self.species}, {self.age} years old"

    def update_details(self, health_record):
        self.health_record = health_record
        self.save()



class Customers(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def login(self):
        # Logic for user login
        pass

    def update_profile(self, email, phone):
        self.email = email
        self.phone = phone
        self.save()
        

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
        # Logic to process payment
        pass

    def refund_payment(self):
        self.status = 'refunded'
        self.save()

