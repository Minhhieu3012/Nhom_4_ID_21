from django.urls import path
from . import views
from .views import(
    PetListView,PetDetailView,PetCreateView,PetUpdateView,PetDeleteView
)
urlpatterns = [
    path('Pet_Cus_Info_Mng/pets/', views.pet_list, name='pet_list'), #url cho pet
    path('Pet_Cus_Info_Mng/customers/', views.customer_list, name='customer_list'), #url cho customer
    
    path('pets/', PetListView.as_view(), name='pet_list'),  # Danh sách Pet
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),  # Chi tiết Pet
    path('pets/add/', PetCreateView.as_view(), name='pet_add'),  # Thêm Pet
    path('pets/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),  # Sửa Pet
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),  # Xóa Pet
]