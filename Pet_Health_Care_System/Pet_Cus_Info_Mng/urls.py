from django.urls import path
from . import views
from .views import (
    CustomerCreateView, CustomerListView, PetListView, PetDetailView, PetCreateView, PetUpdateView,
    PetDeleteView, MedicalRecordListView, AppointmentListView
)

urlpatterns = [
    # Quản lý thú cưng
    path('pets/', PetListView.as_view(), name='pet_list'),  # Danh sách thú cưng
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),  # Chi tiết thú cưng
    path('pets/add/', PetCreateView.as_view(), name='pet_add'),  # Thêm thú cưng
    path('pets/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),  # Sửa thú cưng
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),  # Xóa thú cưng

    # Quản lý khách hàng
    path('customers/', views.customer_list, name='customer_list'),  # Danh sách khách hàng
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),  # Thêm khách hàng

    # Quản lý lịch sử khám chữa bệnh
    path('medical-records/<int:pet_id>/', MedicalRecordListView.as_view(), name='medical_records'),  # Lịch sử khám chữa bệnh

    # Quản lý lịch hẹn
    path('appointments/<int:customer_id>/', AppointmentListView.as_view(), name='appointments'),  # Lịch hẹn
]
