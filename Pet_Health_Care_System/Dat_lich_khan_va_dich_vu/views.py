from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Appointment, Customers, Pets, Vet
from datetime import datetime
from .forms import CustomerRegistrationForm, CustomerLoginForm, CustomerProfileForm

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/home.html')

@login_required
def my_appointments_view(request):
    print(" View function my_appointments_view() is being called.")  # Debug

    if request.method == "POST":
        print(" Received a POST request.")  # Debug

        appointment_id = request.POST.get("cancel_appointment_id")
        print(f" Extracted Appointment ID: {appointment_id}")  # Debug

        if appointment_id:
            appointment = Appointment.objects.filter(pk=appointment_id, pet__owner=request.user).first()
            if appointment:
                print(f" Deleting Appointment: {appointment}")  # Debug
                appointment.delete()
                messages.success(request, "Appointment cancelled successfully.")
            else:
                print(" User does not have permission to cancel this appointment.")  # Debug
                messages.error(request, "You do not have permission to cancel this appointment.")
        else:
            print(" No appointment ID found in POST request.")  # Debug

    appointments = Appointment.objects.filter(pet__owner=request.user)
    return render(request, "Dat_lich_khan_va_dich_vu/my_appointments.html", {"appointments": appointments})

def appointment_view(request):
    if request.method == "POST":
        pet_name = request.POST.get("pet_name", "").strip()
        species = request.POST.get("species", "").strip()
        datetime_str = request.POST.get("datetime", "").strip()
        service_type = request.POST.get("service_type", "").strip()
        vet_name = request.POST.get("vet_name", "").strip()
        additional_message = request.POST.get("message", "").strip()

        owner_email = request.user.email  

        if not pet_name or not species or not datetime_str or not service_type or not vet_name:
            messages.error(request, "All fields are required.")
            return redirect("appointment")

        try:
            appointment_datetime = datetime.strptime(datetime_str, "%m/%d/%Y %H:%M")
        except ValueError:
            messages.error(request, "Invalid date format. Please select a valid date and time.")
            return redirect("appointment")

        pet, created = Pets.objects.get_or_create(
            name=pet_name, 
            owner=request.user,  
            defaults={"species": species, "age": 0, "health_record": ""}
        )

        vet = Vet.objects.filter(name__iexact=vet_name).first()
        if not vet:
            messages.error(request, f"Vet '{vet_name}' not found. Please check the name.")
            return redirect("appointment")

        appointment = Appointment.objects.create(
            pet=pet,
            vet=vet,
            datetime=appointment_datetime,
            service_type=service_type
        )

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
    appointments = Appointment.objects.select_related('pet', 'vet', 'pet__owner').all()  

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

@login_required
def profile_update_view(request):
    customer = request.user

    if request.method == "POST":
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect("profile_update")
    else:
        form = CustomerProfileForm(instance=customer)

    return render(request, "Dat_lich_khan_va_dich_vu/profile_update.html", {"form": form})