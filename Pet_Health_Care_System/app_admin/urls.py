from django.urls import path, include
from . import views

urlpatterns = [
    path('app_admin/', views.Pet, name='Pet'),
    path('app_admin/', views.Owner, name='Owner'),
    path('app_admin/', views.Room, name='Room'),
    path('app_admin/', views.Admission, name='Admission'),
    path('app_admin/', views.Staff, name='Staff'),
    path('app_admin/', views.Invoice, name='Invoice'),
    path('', views.app_admin, name='app_admin'),
]