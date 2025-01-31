from django.urls import path, include
from . import views

urlpatterns = [
    path('app_admin/', views.pet, name='Pet'),
    path('app_admin/', views.owner, name='Owner'),
    path('app_admin/', views.room, name='Room'),
    path('app_admin/', views.admission, name='Admission'),
    path('app_admin/', views.staff, name='Staff'),
    path('app_admin/', views.invoice, name='Invoice'),

    path('', views.app_admin, name='app_admin'),
    path('rooms', views.rooms, name='rooms'),
    path('room-edit/', views.room_edit, name='room-edit'),

] 
