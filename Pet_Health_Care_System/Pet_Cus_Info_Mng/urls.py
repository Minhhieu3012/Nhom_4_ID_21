from django.urls import path
from . import views
from .views import (
    CustomerCreateView,CustomerUpdateView, CustomerDeleteView,
    PetCreateView, PetUpdateView, PetDeleteView,
    MedicalRecordListView, AppointmentListView,
    AppointmentFilterView, AppointmentCreateView
)

urlpatterns = [
    # Quản lý thú cưng
    path('petss/', views.pet_list, name='pet_listt'),  # Danh sách thú cưng
    path('petss/add/', PetCreateView.as_view(), name='pet_add'),  # Thêm thú cưng
    path('petss/<int:pk>/editt/', PetUpdateView.as_view(), name='pet_editt'),  # Sửa thú cưng
    path('petss/<int:pk>/deletee/', PetDeleteView.as_view(), name='pet_deletee'),  # Xóa thú cưng

    # Quản lý khách hàng
    path('customers/', views.customer_list, name='customer_list'),  # Danh sách khách hàng
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),  # Thêm khách hàng
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),  # Sửa khách hàng
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),  # Xóa khách hàng

    # Quản lý lịch sử khám chữa bệnh
    path('petss/medicalRecords-history/<int:pet_id>/', MedicalRecordListView.as_view(), name='medicalRecords_history'),  # Lịch sử khám chữa bệnh

    # Quản lý lịch hẹn
    path('appointments-list/', AppointmentListView.as_view(), name='appointments_list'),
    path('customers/appointments-history/<str:email>/', AppointmentListView.as_view(), name='appointments_history'),  # Lịch hẹn
    path('appointments-filter/', AppointmentFilterView.as_view(), name='appointments_filter'),
    path('appointments-create/', AppointmentCreateView.as_view(), name='appointments_create'),

]
