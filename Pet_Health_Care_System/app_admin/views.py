from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json

# View hiển thị trang admin
def app_admin(request):
    return render(request, 'app_admin/app_admin.html')

# API Đăng nhập
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Kiểm tra tài khoản
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'message': 'Đăng nhập thành công', 'role': user.role})
            return JsonResponse({'error': 'Sai tài khoản hoặc mật khẩu'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dữ liệu không hợp lệ'}, status=400)
    
    return JsonResponse({'error': 'Phương thức không hợp lệ'}, status=405)

# API Đăng xuất
@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Đăng xuất thành công'})
    
    return JsonResponse({'error': 'Phương thức không hợp lệ'}, status=405)
