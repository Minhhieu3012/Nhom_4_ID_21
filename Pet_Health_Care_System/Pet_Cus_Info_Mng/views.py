from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
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
    template_name = 'Pet_Cus_Info_Mng/customer_form.html'  # Tên file template form
    fields = ['lastName', 'firstName', 'email', 'phoneNumber', 'address', 'age', 'gender']  # Các trường được lưu
    success_url = reverse_lazy('customer_list')  # Sau khi tạo thành công, chuyển về danh sách khách hàng
    def form_valid(self, form):
        # Lưu khách hàng
        form.save()
        # Thêm thông báo
        messages.success(self.request, "Khách hàng đã được tạo thành công!")
        # Render lại chính trang thêm khách hàng
        return self.render_to_response(self.get_context_data(form=form))
    
class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['lastName', 'firstName', 'email', 'phoneNumber', 'address', 'age', 'gender']
    template_name = 'Pet_Cus_Info_Mng/customer_edit.html'
    success_url = reverse_lazy('customer_list')  # Chuyển hướng về danh sách khách hàng
    def get_success_url(self):
        return reverse_lazy('customer_edit', kwargs={'pk': self.object.pk})

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'Pet_Cus_Info_Mng/customer_delete.html' #trang xac nhan xoa
    success_url = reverse_lazy('customer_list')
# -------------------------------------------------------------------------------------------

# View cho Pet
def pet_list(request):
    pets = Pet.objects.all() # lay toan bo ds thu cung
    return render(request, 'Pet_Cus_Info_Mng/pets.html',{'pets':pets}) # Render ra template


# CreateView cho Pet
class PetCreateView(CreateView):
    model = Pet
    template_name = 'Pet_Cus_Info_Mng/pet_form.html' # form hien thi de them pet
    fields = ['name','species','gender','date_of_birth','age','health_status','owner']
    success_url = reverse_lazy('pet_list') # chuyen huong sau khi them thanh cong
    def form_valid(self, form):
        messages.success(self.request, "Thú cưng đã được thêm thành công!")
        return super().form_valid(form)


# UpdateView cho Pet
class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'Pet_Cus_Info_Mng/pet_edit.html' # Su dung chung form voi createview
    fields = ['name','species','gender','date_of_birth','age','health_status','owner']
    success_url = reverse_lazy('pet_list')

# DeleteView cho Pet
class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'Pet_Cus_Info_Mng/pet_delete.html' #trang xac nhan xoa
    success_url = reverse_lazy('pet_list')

# -------------------------------------------------------------------------------------------

class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'Pet_Cus_Info_Mng/medical_records.html'  # ten file template de hien thi lich su
    context_object_name = 'medical_records'  # ten bien trong template

    def get_queryset(self):
        # Neu muon chi hien thi lich su cua 1 thu cung, su dung filter
        pet_id = self.kwargs.get('pet_id')  # Lấy ID thú cưng từ URL
        return MedicalRecord.objects.filter(pet_id=pet_id).order_by('-date')  # Lịch sử theo thứ tự mới nhất
    
# -------------------------------------------------------------------------------------------

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'Pet_Cus_Info_Mng/appointments.html'  # Tên file template hiển thị lịch hẹn
    context_object_name = 'appointments'  # Tên biến trong template

    def get_queryset(self):
        # Hiển thị lịch hẹn theo khách hàng
        customer_id = self.kwargs.get('customer_id')  # Lấy ID khách hàng từ URL
        return Appointment.objects.filter(customer_id=customer_id).order_by('-date', '-time')  # Lịch hẹn mới nhất
