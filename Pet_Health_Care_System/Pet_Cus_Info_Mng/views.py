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
def filter_appointments(request):
    appointments = Appointment.objects.all()
    if 'date' in request.GET:
        appointments = appointments.filter(date=request.GET['date'])
    if 'status' in request.GET:
        appointments = appointments.filter(status=request.GET['status'])
    return render(request, 'Pet_Cus_Info_Mng/appointments-list.html', {'appointments': appointments})
    

def send_appointment_notification(appointment):
    send_mail(
        'Lịch hẹn mới',
        f'Bạn đã đặt lịch hẹn thành công vào {appointment.date} lúc {appointment.time}.',
        'noreply@example.com',
        [appointment.customer.email],
    )
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            customer_id = form.cleaned_data['customer']
            pet_id = form.cleaned_data['pet']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            status = form.cleaned_data['status']

            # Tìm đối tượng Customer và Pet
            customer = get_object_or_404(Customer, id=customer_id)
            pet = get_object_or_404(Pet, id=pet_id)

            # Tạo và lưu lịch hẹn
            appointment = Appointment(
                customer=customer,
                pet=pet,
                date=date,
                time=time,
                status=status
            )
            appointment.save()
            return redirect('appointments_list')
    else:
        form = AppointmentsForm()

    return render(request, 'Pet_Cus_Info_Mng/appointments-create.html', {'form': form})


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
