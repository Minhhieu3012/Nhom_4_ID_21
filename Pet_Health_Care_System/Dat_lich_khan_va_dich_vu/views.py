from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment, Customers, Pets
def home(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/home.html')

def test(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/test.html')

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
    appointments = Appointment.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/appointments.html', {'appointments': appointments})

def list_customers(request):
    customers = Customers.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/customers.html', {'customers': customers})

def list_pets(request):
    pets = Pets.objects.all()
    return render(request, 'Dat_lich_khan_va_dich_vu/pets.html', {'pets': pets})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'Dat_lich_khan_va_dich_vu/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')