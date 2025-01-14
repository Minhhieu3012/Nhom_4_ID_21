from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Pet, Customer, MedicalRecord, Appointment


# Create your views here.
# View cho Customer
def customer_list(request):
    customers = Customer.objects.all() # lay toan bo ds khach hang
    return render(request, 'Pet_Cus_Info_Mng/customers.html', {'customers': customers})

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'phone_number', 'address', 'gender']
    success_url = reverse_lazy('customer_list')


# View cho Pet
def pet_list(request):
    pets = Pet.objects.all() # lay toan bo ds thu cung
    return render(request, 'Pet_Cus_Info_Mng/pets.html',{'pets':pets}) # Render ra template

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


class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medical_records.html'  # ten file template de hien thi lich su
    context_object_name = 'medical_records'  # ten bien trong template

    def get_queryset(self):
        # Neu muon chi hien thi lich su cua 1 thu cung, su dung filter
        pet_id = self.kwargs.get('pet_id')  # Lấy ID thú cưng từ URL
        return MedicalRecord.objects.filter(pet_id=pet_id).order_by('-date')  # Lịch sử theo thứ tự mới nhất
    

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments.html'  # Tên file template hiển thị lịch hẹn
    context_object_name = 'appointments'  # Tên biến trong template

    def get_queryset(self):
        # Hiển thị lịch hẹn theo khách hàng
        customer_id = self.kwargs.get('customer_id')  # Lấy ID khách hàng từ URL
        return Appointment.objects.filter(customer_id=customer_id).order_by('-date', '-time')  # Lịch hẹn mới nhất
