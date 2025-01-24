from django.shortcuts import render, get_object_or_404
from .models import Staff, Schedule

# Danh sách nhân viên
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff_management/staff_list.html', {'staff': staff})

# Chi tiết lịch làm việc của nhân viên
def staff_schedule(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    schedules = staff.schedules.all()
    return render(request, 'staff_management/staff_schedule.html', {'staff': staff, 'schedules': schedules})
