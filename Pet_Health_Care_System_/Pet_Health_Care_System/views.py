from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Đảm bảo tên file đúng
