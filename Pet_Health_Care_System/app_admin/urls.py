from django.urls import path, include
from . import views
from .views import admission_list, admission_create, admission_discharge, invoice_detail, invoice_payment
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('app_admin/', views.pet, name='Pet'),
    path('app_admin/', views.owner, name='Owner'),
    path('app_admin/', views.room, name='Room'),
    path('app_admin/', views.admission, name='Admission'),
    path('app_admin/', views.staff, name='Staff'),
    path('app_admin/', views.invoice, name='Invoice'),

    path('', views.app_admin, name='app_admin'),
    path('rooms', views.rooms, name='rooms'),
    path('room-edit/<int:id>/', views.room_edit, name='room-edit'),
    path('room-add/', views.room_add, name='room-add'),
    path('room-delete/<int:id>/', views.room_delete, name='room-delete'),


    # *** DỊCH VỤ NHẬP VIỆN
    
    path("admission-list", views.admission_list, name="admission-list"),
    path("admission-create", views.admission_create, name="admission-create"),
    path("admission-discharge/<int:id>/", views.admission_discharge, name="admission-discharge"),
    
    path("invoice-detail/<int:id>/", views.invoice_detail, name="invoice-detail"),
    path("invoice-payment/<int:id>/", views.invoice_payment, name="invoice-payment"),
  
    path('', views.app_admin, name='app_admin'),
] 
