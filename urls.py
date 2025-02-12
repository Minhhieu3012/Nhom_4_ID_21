from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),
]
