from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Dat_lich_khan_va_dich_vu/home.html')

