from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Pet, Customer

# Create your views here.

# View cho Pet
def pet_list(request):
    pets = Pet.objects.all() # lay toan bo ds thu cung
    return render(request, 'pets.html',{'pets':pets}) # Render ra template

# View cho Customer
def customer_list(request):
    customers = Customer.objects.all() # lay toan bo ds khach hang
    return render(request, 'customers.html',{'customers':customers})

# ListView cho Pet
class PetListView(ListView):
    model = Pet
    template_name = 'pets.html' # Ten file template
    context_object_name = 'pets'

# DetailView cho Pet
class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_detail.html' 
    context_object_name = 'pet'

# CreateView cho Pet
class PetCreateView(CreateView):
    model = Pet
    template_name = 'pet_form.html' # form hien thi de them pet
    fields = ['name','species','gender','date_of_birth','age','health_status','owner']
    success_url = reverse_lazy('pet_list') # chuyen huong sau khi them thanh cong

# UpdateView cho Pet
class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'pet_form.html' # Su dung chung form voi createview
    fields = ['name','species','gender','date_of_birth','age','health_status','owner']
    success_url = reverse_lazy('pet_list')

# DeleteView cho Pet
class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pet_confirm.html' #trang xac nhan xoa
    success_url = reverse_lazy('pet_list')