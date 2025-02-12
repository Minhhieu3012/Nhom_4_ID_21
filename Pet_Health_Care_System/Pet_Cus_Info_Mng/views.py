from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import AppointmentsForm
from .models import Pet, Customer, MedicalRecord, Appointment
from django.core.cache import cache
from django.views.decorators.cache import cache_page

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
    template_name = 'Pet_Cus_Info_Mng/medicalRecords-history.html'  # ten file template de hien thi lich su
    context_object_name = 'medical_records'  # ten bien trong template

    def get_queryset(self):
        # Neu muon chi hien thi lich su cua 1 thu cung, su dung filter
        pet_id = self.kwargs.get('pet_id')  # Lấy ID thú cưng từ URL
        return MedicalRecord.objects.filter(pet_id=pet_id).order_by('-date')  # Lịch sử theo thứ tự mới nhất
    
# -------------------------------------------------------------------------------------------

class AppointmentsHistoryView(ListView):
    def get(self, request, email):
        # Lọc lịch hẹn theo email và xử lý lỗi nếu không tìm thấy
        appointments = Appointment.objects.filter(customer__email=email)
        if not appointments.exists():
            return render(request, 'appointments-history.html', {
                'appointments': None,
                'error_message': 'Không có lịch hẹn nào được tìm thấy cho email này.'
            })
        return render(request, 'appointments-history.html', {'appointments': appointments})
    def appointments_history(request, email):
        # Lấy lịch sử đặt hẹn từ database dựa trên email
        appointments = Appointment.objects.filter(customer__email=email)

        context = {
            'email': email,
            'appointments': appointments,
        }
        return render(request, 'appointments_history.html', context)
    
class AppointmentListView(ListView):
    def appointments_list(request):
        appointments = Appointment.objects.all() # lay toan bo ds thu cung
        return render(request, 'Pet_Cus_Info_Mng/appointments-list.html',{'appointments':appointments}) # Render ra template
    def get(self, request, **kwargs):
        email = kwargs.get('email')  # Lấy email từ URL
        if email:
            # Lọc lịch hẹn theo email
            appointments = Appointment.objects.filter(customer__email=email)
            template_name = 'Pet_Cus_Info_Mng/appointments-history.html'
        else:
            # Lấy tất cả lịch hẹn
            appointments = Appointment.objects.all()
            template_name = 'Pet_Cus_Info_Mng/appointments-list.html'

        return render(request, template_name, {'appointments': appointments})


# chức năng lọc lịch hẹn
class AppointmentFilterView(ListView):
    model = Appointment
    template_name = 'Pet_Cus_Info_Mng/appointments-filter.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        # Lọc dữ liệu dựa trên tham số GET
        queryset = Appointment.objects.all()
        date = self.request.GET.get('date')
        status = self.request.GET.get('status')
        if date:
            queryset = queryset.filter(date=date)
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
        customer_email = form.cleaned_data.get('customer')  # Email của khách hàng
        pet_id = form.cleaned_data.get('pet')  # ID của thú cưng
        date = form.cleaned_data.get('date')
        time = form.cleaned_data.get('time')
        status = form.cleaned_data.get('status')

        # Kiểm tra dữ liệu hợp lệ
        customer = Customer.objects.filter(email=customer_email).first()
        if not customer:
            return HttpResponseBadRequest("Khách hàng không tồn tại.")  # Trả về lỗi nếu không tìm thấy khách hàng

        pet = Pet.objects.filter(id=pet_id).first()
        if not pet:
            return HttpResponseBadRequest("Thú cưng không tồn tại.")  # Trả về lỗi nếu không tìm thấy thú cưng

        # Tạo và lưu đối tượng Appointment
        Appointment.objects.create(
            customer=customer,
            pet=pet,
            date=date,
            time=time,
            status=status
        )

        # Redirect đến success_url
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        # Truyền danh sách khách hàng và thú cưng vào template
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()  # Lấy danh sách khách hàng
        context['pets'] = Pet.objects.all()  # Lấy danh sách thú cưng
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)  # Loại bỏ instance nếu tồn tại
        return kwargs
    
# -------------------------------------------------------------------------------------------

