from django.contrib import admin
from .models import Pet, MedicalRecord, TreatmentProgress, Medication, Notification

admin.site.register(Pet)
admin.site.register(MedicalRecord)
admin.site.register(TreatmentProgress)
admin.site.register(Medication)
admin.site.register(Notification)
