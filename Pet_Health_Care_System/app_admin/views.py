from django.shortcuts import render
from django.http import HttpResponse

def Pet(request):
    return HttpResponse("Hello world!")
def Owner(request):
    return HttpResponse("Hello world!")
def Room(request):
    return HttpResponse("Hello world!")
def Admission(request):
    return HttpResponse("Hello world!")
def Staff(request):
    return HttpResponse("Hello world!")
def Invoice(request):
    return HttpResponse("Hello world!")
def app_admin (request):
    return render (request, 'app_admin/app_admin.html')