from django.urls import path
from . import views
from .views import(
    CustomerCreateView, PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView, MedicalRecordListView, AppointmentListView
)
urlpatterns = [
    path('Pet_Cus_Info_Mng/pets/', views.pet_list, name='pet_list'), #url cho pet
    path('Pet_Cus_Info_Mng/customers/', views.customer_list, name='customer_list'), #url cho customer
    
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),
    path('pets/', PetListView.as_view(), name='pet_list'),  # Danh sách Pet
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),  # Chi tiết Pet
    path('pets/add/', PetCreateView.as_view(), name='pet_add'),  # Thêm Pet
    path('pets/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),  # Sửa Pet
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),  # Xóa Pet
    path('medical-records/<int:pet_id>/', MedicalRecordListView.as_view(), name='medical_records'),
    path('appointments/<int:customer_id>/', AppointmentListView.as_view(), name='appointments'),
]


