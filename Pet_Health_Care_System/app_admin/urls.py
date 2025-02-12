from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.app_admin, name='app_admin'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
