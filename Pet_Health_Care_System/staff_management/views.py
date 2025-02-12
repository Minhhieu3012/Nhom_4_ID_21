from django.shortcuts import render, get_object_or_404, redirect
from .models import Staff, WorkSchedule, WorkShift
from .forms import StaffForm, WorkScheduleForm, WorkShiftForm

def staff_detail(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    return render(request, 'staff_management/staff_detail.html', {'staff': staff})

def staff_edit(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_detail', staff_id=staff.id)
    else:
        form = StaffForm(instance=staff)

    return render(request, 'staff_management/staff_form.html', {'form': form, 'staff': staff})



# --- Staff Views ---
def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'staff_list.html', {'staffs': staffs})

def staff_detail(request, id):
    staff = get_object_or_404(Staff, id=id)
    return render(request, 'staff_detail.html', {'staff': staff})

def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_form.html', {'form': form})

def staff_update(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_form.html', {'form': form})

def staff_delete(request, id):
    staff = get_object_or_404(Staff, id=id)
    staff.delete()
    return redirect('staff_list')

# --- WorkSchedule Views ---
def work_schedule_list(request):
    schedules = WorkSchedule.objects.all()
    return render(request, 'work_schedule_list.html', {'schedules': schedules})

def work_schedule_detail(request, id):
    schedule = get_object_or_404(WorkSchedule, id=id)
    return render(request, 'work_schedule_detail.html', {'schedule': schedule})

def work_schedule_create(request):
    if request.method == 'POST':
        form = WorkScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_schedule_list')
    else:
        form = WorkScheduleForm()
    return render(request, 'work_schedule_form.html', {'form': form})

def work_schedule_update(request, id):
    schedule = get_object_or_404(WorkSchedule, id=id)
    if request.method == 'POST':
        form = WorkScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('work_schedule_list')
    else:
        form = WorkScheduleForm(instance=schedule)
    return render(request, 'work_schedule_form.html', {'form': form})

def work_schedule_delete(request, id):
    schedule = get_object_or_404(WorkSchedule, id=id)
    schedule.delete()
    return redirect('work_schedule_list')

# --- WorkShift Views ---
def work_shift_list(request):
    shifts = WorkShift.objects.all()
    return render(request, 'work_shift_list.html', {'shifts': shifts})

def work_shift_detail(request, id):
    shift = get_object_or_404(WorkShift, id=id)
    return render(request, 'work_shift_detail.html', {'shift': shift})

def work_shift_create(request):
    if request.method == 'POST':
        form = WorkShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_shift_list')
    else:
        form = WorkShiftForm()
    return render(request, 'work_shift_form.html', {'form': form})

def work_shift_update(request, id):
    shift = get_object_or_404(WorkShift, id=id)
    if request.method == 'POST':
        form = WorkShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect('work_shift_list')
    else:
        form = WorkShiftForm(instance=shift)
    return render(request, 'work_shift_form.html', {'form': form})

def work_shift_delete(request, id):
    shift = get_object_or_404(WorkShift, id=id)
    shift.delete()
    return redirect('work_shift_list')


def staff_list(request):
    return render(request, 'staff_management/staff_list.html')

def staff_detail(request):
    return render(request, 'staff_management/staff_detail.html')

def work_schedule_list(request):
    return render(request, 'staff_management/work_schedule_list.html')

def work_shift_list(request):
    return render(request, 'staff_management/work_shift_list.html')

