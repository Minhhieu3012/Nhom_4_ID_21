from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app_admin(request):
    return render(request,'app_admin/app_admin.html')