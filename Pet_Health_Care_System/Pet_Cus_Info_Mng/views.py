from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import AppointmentsForm
from .models import Pet, Customer, MedicalRecord, Appointment, Transaction
from django.core.mail import send_mail
from django.core.exceptions import ValidationError


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
        messages.success(self.request, "Thông tin khách hàng đã được cập nhật thành công!")
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
class PetCreateView(CreateView):
    model = Pet
    template_name = 'Pet_Cus_Info_Mng/pet_form.html'
    fields = ['name', 'species', 'gender', 'dateOfBirth', 'age', 'healthStatus', 'owner']
    success_url = reverse_lazy('pet_list')
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thú cưng đã được tạo thành công!")
        # Render lại chính trang thêm thú cưng
        return self.render_to_response(self.get_context_data(form=form))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()  # Truyền danh sách khách hàng vào context
        return context
class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'Pet_Cus_Info_Mng/pet_edit.html'  # Sử dụng chung form với CreateView
    fields = ['name', 'species', 'gender', 'healthStatus', 'owner']
    success_url = reverse_lazy('pet_list')
    def get_success_url(self):
        messages.success(self.request, "Thông tin thú cưng đã được cập nhật thành công!")
        return reverse_lazy('pet_edit', kwargs={'pk': self.object.pk})
    
class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'Pet_Cus_Info_Mng/pet_delete.html' #trang xac nhan xoa
    success_url = reverse_lazy('pet_list')

# -------------------------------------------------------------------------------------------
class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'Pet_Cus_Info_Mng/medicalRecords_history.html'  # ten file template de hien thi lich su
    context_object_name = 'medical_records'  # ten bien trong template

    def get_queryset(self):
        # Neu muon chi hien thi lich su cua 1 thu cung, su dung filter
        pet_id = self.kwargs.get('pet_id')  # Lấy ID thú cưng từ URL
        return MedicalRecord.objects.filter(pet_id=pet_id).order_by('-date')  # Lịch sử theo thứ tự mới nhất
    
# -------------------------------------------------------------------------------------------
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'Pet_Cus_Info_Mng/appointments-list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.all().order_by('-date', '-time')
    

# chức năng lọc lịch hẹn
class AppointmentFilterView(ListView):
    model = Appointment
    template_name = 'Pet_Cus_Info_Mng/appointments-list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        queryset = Appointment.objects.all()
        # Lọc theo ngày
        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(date=date)
        # Lọc theo trạng thái
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
    

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentsForm
    template_name = 'Pet_Cus_Info_Mng/appointments-create.html'
    success_url = reverse_lazy('appointments_list')

    def form_valid(self, form):
        # Lấy dữ liệu từ form
        customer_email = form.cleaned_data['customer_email']  # Thay đổi để lấy email
        pet_id = form.cleaned_data['pet']

        # Tìm đối tượng Customer bằng email
        customer = get_object_or_404(Customer, email=customer_email)  # Tìm bằng email
        pet = get_object_or_404(Pet, id=pet_id)

        # Tạo đối tượng Appointment
        appointment = form.save(commit=False)
        appointment.customer = customer
        appointment.pet = pet
        appointment.save()

        return super().form_valid(form)
    # loại bỏ instance
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)  # Loại bỏ tham số instance nếu tồn tại
        return kwargs

# -------------------------------------------------------------------------------------------

class TransactionListView(ListView):
    model = Transaction
    template_name = 'Pet_Cus_Info_Mng/transaction_history.html'  # Tên file template
    context_object_name = 'transactions'  # Tên biến context để sử dụng trong template
    success_url = reverse_lazy('transactions')  # URL sau khi thành công
    ordering = ['-created_at']  # Sắp xếp theo thời gian mới nhất

    def get_queryset(self):
        # Lọc danh sách giao dịch nếu cần
        queryset = super().get_queryset()
        return queryset
