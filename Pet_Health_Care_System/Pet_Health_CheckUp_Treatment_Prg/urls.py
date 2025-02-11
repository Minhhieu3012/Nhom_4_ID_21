from django.urls import path
from . import views

urlpatterns = [
    path('Pet_Health_CheckUp_Treatment_Prg/', views.Pet_Health_CheckUp_Treatment_Prg, name='Pet_Health_CheckUp_Treatment_Prg'),
]