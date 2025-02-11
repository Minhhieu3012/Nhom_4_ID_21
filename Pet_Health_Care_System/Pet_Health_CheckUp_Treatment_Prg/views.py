# views.py
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from .models import MedicalRecord, Medication, Treatment, Notification
from .forms import MedicalRecordForm, NotificationForm, TreatmentForm

# ----------------------------------------------------------------------------------------------------

def medical_record_list(request):
    # Lấy tất cả bệnh án từ cơ sở dữ liệu
    records = MedicalRecord.objects.all()
    return render(request, 'medical_record_list.html', {'records': records})

def medical_record_detail(request, record_id):
    # Lấy bệnh án theo ID hoặc trả về lỗi 404 nếu không tìm thấy
    record = get_object_or_404(MedicalRecord, pk=record_id)
    return render(request, 'medical_record_detail.html', {'record': record})

def medical_record_create(request):
    # Nếu phương thức yêu cầu là POST (người dùng đã gửi form)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu bệnh án mới vào cơ sở dữ liệu
            return redirect('medical_record_list')  # Chuyển hướng đến danh sách bệnh án
    else:
        form = MedicalRecordForm()  # Tạo form mới khi yêu cầu là GET

    return render(request, 'medical_record_form.html', {'form': form})

def medical_record_edit(request, record_id):
    # Lấy bệnh án theo ID
    record = get_object_or_404(MedicalRecord, pk=record_id)

    # Nếu phương thức yêu cầu là POST (người dùng đã gửi form)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()  # Lưu các thay đổi vào cơ sở dữ liệu
            return redirect('medical_record_list')  # Chuyển hướng đến danh sách bệnh án
    else:
        form = MedicalRecordForm(instance=record)  # Tạo form từ dữ liệu hiện tại của bệnh án

    return render(request, 'medical_record_form.html', {'form': form})

def medical_history_list(request, pet_id):
    history = MedicalHistory.objects.filter(pet_id=pet_id)  # Lọc theo thú cưng
    return render(request, 'medical_history_list.html', {'history': history})

#------------------------------------------------------------------------------------------------------------

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medication_list.html', {'medications': medications})

def medication_create(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medication_list')
    else:
        form = MedicationForm()

    return render(request, 'medication_form.html', {'form': form})

# ----------------------------------------------------------------------------------------------------

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notification_list.html', {'notifications': notifications})


def notification_create(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu thông báo mới vào cơ sở dữ liệu
            return redirect('notification_list')
    else:
        form = NotificationForm()

    return render(request, 'notification_form.html', {'form': form})



# ----------------------------------------------------------------------------------------------------


def treatment_list(request):
    treatments = Treatment.objects.all()  # Lấy tất cả tiến trình điều trị
    return render(request, 'treatment_list.html', {'treatments': treatments})


def treatment_create(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu tiến trình điều trị mới vào cơ sở dữ liệu
            return redirect('treatment_list')
    else:
        form = TreatmentForm()  # Tạo form mới

    return render(request, 'treatment_form.html', {'form': form})


def treatment_edit(request, treatment_id):
    treatment = get_object_or_404(Treatment, pk=treatment_id)

    if request.method == 'POST':
        form = TreatmentForm(request.POST, instance=treatment)
        if form.is_valid():
            form.save()  # Lưu các thay đổi vào cơ sở dữ liệu
            return redirect('treatment_list')  # Chuyển hướng đến danh sách tiến trình điều trị
    else:
        form = TreatmentForm(instance=treatment)  # Tạo form từ dữ liệu hiện tại của tiến trình điều trị

    return render(request, 'treatment_form.html', {'form': form})


def treatment_detail(request, treatment_id):
    treatment = get_object_or_404(Treatment, pk=treatment_id)  # Lấy tiến trình điều trị theo ID
    return render(request, 'treatment_detail.html', {'treatment': treatment})