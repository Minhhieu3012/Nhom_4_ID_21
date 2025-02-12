from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import AuditLog

User = get_user_model()

def log_action(user, action):
    AuditLog.objects.create(user=user, action=action)

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            log_action(request.user, f"Tạo tài khoản {form.cleaned_data['username']}")
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'accounts/user_form.html', {'form': form})

@login_required
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    log_action(request.user, f"Xóa tài khoản {user.username}")
    user.delete()
    return redirect('user_list')
