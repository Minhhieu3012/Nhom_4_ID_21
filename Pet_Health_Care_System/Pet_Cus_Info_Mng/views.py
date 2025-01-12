from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet, Customer

# Create your views here.

#View cho Pet
def pet_list(request):
    pets = Pet.objects.all() #lay toan bo ds thu cung
    return render(request, 'pets.html',{'pets':pets}) #Render ra template

#View cho Customer
def customer_list(request):
    customers = Customer.objects.all() #lay toan bo ds khach hang
    return render(request, 'customers.html',{'customers':customers})