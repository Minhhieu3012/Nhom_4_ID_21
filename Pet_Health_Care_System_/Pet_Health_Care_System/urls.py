from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Gán trang chủ vào '/'
    path('feedback/', include('Service_Feedback.urls')),  # Nếu có feedback app
]
