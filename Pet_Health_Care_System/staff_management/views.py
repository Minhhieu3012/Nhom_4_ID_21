from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Staff, WorkingSchedule
from .forms import StaffForm, WorkingScheduleForm

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
