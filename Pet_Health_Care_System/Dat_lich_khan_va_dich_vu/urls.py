from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('customers/', views.list_customers, name='list_customers'),
    path('pets/', views.list_pets, name='list_pets'),
]
