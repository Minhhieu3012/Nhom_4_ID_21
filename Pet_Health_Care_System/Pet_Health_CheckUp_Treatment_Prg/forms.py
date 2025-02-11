# forms.py
from django import forms
from .models import Pet, MedicalRecord, TreatmentProgress, Medication


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'current_health_status']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['pet', 'date', 'symptoms', 'disease', 'vet_notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # sử dụng date picker của HTML5
        }

class TreatmentProgressForm(forms.ModelForm):
    class Meta:
        model = TreatmentProgress
        fields = ['pet', 'medical_record', 'medication', 'treatment_method', 'next_appointment_date', 'updated_health_status']
        widgets = {
            'next_appointment_date': forms.DateInput(attrs={'type': 'date'})
        }

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'description', 'dosage_info']
