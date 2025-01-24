from django.shortcuts import render
from .models import Appointment, Customers, Pets

def home(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/home.html')

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/appointments.html', {'appointments': appointments})

def list_customers(request):
    customers = Customers.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/customers.html', {'customers': customers})

def list_pets(request):
    pets = Pets.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/pets.html', {'pets': pets})