from django.urls import path
from . import views

urlpatterns = [
    path('Pet_Cus_Info_Mng/pets/', views.pet_list, name='pet_list'), #url cho pet
    path('Pet_Cus_Info_Mng/customers/', views.customer_list, name='customer_list'), #url cho customer
]