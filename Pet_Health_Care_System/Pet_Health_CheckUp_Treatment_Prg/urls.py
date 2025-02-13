# urls.py
from django.urls import path
from . import views


urlpatterns = [
    # URL cho Pet
    path('pets/', views.PetListView.as_view(), name='pet_list'),
    path('pets/new/', views.PetCreateView.as_view(), name='pet_create'),
    path('pets/<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('pets/<int:pk>/edit/', views.PetUpdateView.as_view(), name='pet_update'),
    path('pets/<int:pk>/delete/', views.PetDeleteView.as_view(), name='pet_delete'),

    # Các URL cho Medical Record
    path('pets/medical-records/<int:pet_id>/', views.MedicalRecordListView.as_view(), name='medical_record_list'),
    path('medical-records/new/', views.MedicalRecordCreateView.as_view(), name='medical_record_create'),
    path('medical-records/<int:pk>/edit/', views.MedicalRecordUpdateView.as_view(), name='medical_record_update'),
    path('medical-records/<int:pk>/delete/', views.MedicalRecordDeleteView.as_view(), name='medical_record_delete'),

    # Các URL cho Treatment Progress
    path('pets/treatment-progress/<int:pet_id>/', views.TreatmentProgressListView.as_view(), name='treatment_progress_list'),
    path('treatment-progress/new/', views.TreatmentProgressCreateView.as_view(), name='treatment_progress_create'),
    path('treatment-progress/<int:pk>/edit/', views.TreatmentProgressUpdateView.as_view(), name='treatment_progress_update'),
    path('treatment-progress/<int:pk>/delete/', views.TreatmentProgressDeleteView.as_view(), name='treatment_progress_delete'),

    # Các URL cho Medication
    path('medications/', views.MedicationListView.as_view(), name='medication_list'),
    path('medications/new/', views.MedicationCreateView.as_view(), name='medication_create'),
    path('medications/<int:pk>/edit/', views.MedicationUpdateView.as_view(), name='medication_update'),
    path('medications/<int:pk>/delete/', views.MedicationDeleteView.as_view(), name='medication_delete'),
]
