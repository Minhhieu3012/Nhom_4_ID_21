# admin.py
from django.contrib import admin
from .models import Pet, MedicalRecord, Treatment, Medication, Notification, MedicalHistory

# Đăng ký các model với Django Admin
admin.site.register(Pet, MedicalRecord, Treatment, Medication, Notification, MedicalHistory)






