from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Staff, WorkingSchedule
from .forms import StaffForm, WorkingScheduleForm


from django.shortcuts import render
from django.views.generic import DetailView
from .models import Staff, Appointment, WorkingSchedule, Role, AppointmentHistory, Notification

# View cho Staff
class StaffDetailView(DetailView):
    model = Staff
    template_name = 'staff_detail.html'
    context_object_name = 'staff'

# View cho Appointment
class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'
    context_object_name = 'appointment'

# View cho WorkingSchedule
class WorkingScheduleDetailView(DetailView):
    model = WorkingSchedule
    template_name = 'working_schedule_detail.html'
    context_object_name = 'schedule'

# View cho Role
class RoleDetailView(DetailView):
    model = Role
    template_name = 'role_detail.html'
    context_object_name = 'role'

# View cho AppointmentHistory
class AppointmentHistoryDetailView(DetailView):
    model = AppointmentHistory
    template_name = 'appointment_history_detail.html'
    context_object_name = 'appointment_history'

# View cho Notification
class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'


# Danh sách nhân viên
class StaffListView(ListView):
    model = Staff
    template_name = 'staff_list.html'
    context_object_name = 'staffs'

# Chi tiết nhân viên
class StaffDetailView(DetailView):
    model = Staff
    template_name = 'staff_detail.html'

# Thêm nhân viên
class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff_form.html'
    success_url = reverse_lazy('staff_list')

# Cập nhật nhân viên
class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'staff_form.html'
    success_url = reverse_lazy('staff_list')

# Xóa nhân viên
class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'staff_confirm_delete.html'
    success_url = reverse_lazy('staff_list')


def staff_list(request):
    return render(request, 'staff_management/staff_list.html')

def staff_detail(request):
    return render(request, 'staff_management/staff_detail.html')

def schedule_list(request):
    return render(request, 'staff_management/schedule_list.html')