from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Appointment, Customers, Pets, Vet
from datetime import datetime
from .forms import CustomerRegistrationForm, CustomerLoginForm

from django.contrib.auth.decorators import login_required

@login_required

def home(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/home.html')

def appointment_view(request):
    if request.method == "POST":
        pet_name = request.POST.get("pet_name", "").strip()
        species = request.POST.get("species", "").strip()
        datetime_str = request.POST.get("datetime", "").strip()
        service_type = request.POST.get("service_type", "").strip()
        vet_name = request.POST.get("vet_name", "").strip()
        additional_message = request.POST.get("message", "").strip()

        #  Lấy email khách hàng từ tài khoản đăng nhập
        owner_email = request.user.email  

        # Kiểm tra dữ liệu hợp lệ
        if not pet_name or not species or not datetime_str or not service_type or not vet_name:
            messages.error(request, "All fields are required.")
            return redirect("appointment")

        # Chuyển đổi datetime string sang dạng Python datetime object
        try:
            appointment_datetime = datetime.strptime(datetime_str, "%m/%d/%Y %H:%M")
        except ValueError:
            messages.error(request, "Invalid date format. Please select a valid date and time.")
            return redirect("appointment")

        # Tìm hoặc tạo thú cưng
        pet, created = Pets.objects.get_or_create(
            name=pet_name, 
            owner=request.user,  #  Gán khách hàng hiện tại làm chủ
            defaults={"species": species, "age": 0, "health_record": ""}
        )

        # Tìm bác sĩ thú y
        vet = Vet.objects.filter(name__iexact=vet_name).first()
        if not vet:
            messages.error(request, f"Vet '{vet_name}' not found. Please check the name.")
            return redirect("appointment")

        #  Tạo và lưu lịch hẹn
        appointment = Appointment.objects.create(
            pet=pet,
            vet=vet,
            datetime=appointment_datetime,
            service_type=service_type
        )

        #  Lưu tin nhắn bổ sung vào hồ sơ thú cưng
        if additional_message:
            pet.health_record += f"\nAppointment Note: {additional_message}"
            pet.save()

        messages.success(request, f"Appointment scheduled successfully for {pet_name}!")
        return redirect("appointment")

    return render(request, "Dat_lich_khan_va_dich_vu/appointment.html")

def main(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/main.html')

def blogsingle(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/blogsingle.html')

def contact(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/contact.html')

def pricing(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/pricing.html')

def gallery(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/gallery.html')

def services(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/services.html')

def vet(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/vet.html')

def blog(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/blog.html')

def about(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/about.html')

def list_appointments(request):
    appointments = Appointment.objects.select_related('pet', 'vet', 'pet__owner').all()  # Ensure pet and owner are retrieved

    appointment_data = []
    for appointment in appointments:
        pet = appointment.pet
        owner_email = pet.owner.email if pet.owner else "No Owner Found"

        appointment_data.append({
            "customer": owner_email,
            "pet_name": pet.name,
            "pet_species": pet.species,
            "vet_name": appointment.vet.name,
            "service_type": appointment.service_type,
            "appointment_date": appointment.datetime,
        })

    return render(request, 'Dat_lich_khan_va_dich_vu/appointments.html', {'appointments': appointment_data})

def list_customers(request):
    customers = Customers.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/customers.html', {'customers': customers})

def list_pets(request):
    pets = Pets.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/pets.html', {'pets': pets})


def register_view(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("home")
    else:
        form = CustomerRegistrationForm()
    return render(request, "Dat_lich_khan_va_dich_vu/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
    else:
        form = CustomerLoginForm()
    return render(request, "Dat_lich_khan_va_dich_vu/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("login")

def my_appointments_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    appointments = Appointment.objects.filter(pet__owner=request.user)
    return render(request, "Dat_lich_khan_va_dich_vu/my_appointments.html", {"appointments": appointments})