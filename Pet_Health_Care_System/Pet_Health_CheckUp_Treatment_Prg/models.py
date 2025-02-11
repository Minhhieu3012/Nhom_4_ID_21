from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100, blank=False)
    species = models.CharField(max_length=255, blank=False, null=True)
    age = models.PositiveIntegerField(blank=False)
    current_health_status = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.name
    

class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medical_records')
    date = models.DateField(blank=False)
    symptoms = models.TextField(blank=False)
    disease = models.CharField(max_length=255, blank=False)
    # Đã thêm default='' để tránh lỗi khi migration
    vet_notes = models.TextField(blank=False, null=True)

    def __str__(self):
        return f"{self.pet.name} - {self.date}"


class TreatmentProgress(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='treatment_progress')
    medical_record = models.ForeignKey(
        MedicalRecord, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='treatment_progress'
    )
    medication = models.ManyToManyField('Medication', blank=True)
    treatment_method = models.TextField()
    next_appointment_date = models.DateField(null=True, blank=True)
    updated_health_status = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Treatment for {self.pet.name} on {self.updated_at}"


class Medication(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    dosage_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField(null=True)
    sent_date = models.DateTimeField(auto_now_add=True, null=True)
    is_read = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"Notification for {self.pet.name} on {self.sent_date}"
