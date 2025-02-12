from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile_update.html', views.profile_update_view, name='profile_update'),
    path('login.html', views.login_view, name='login'),
    path('my_appointments.html', views.my_appointments_view, name='my_appointments'),
    path('', views.list_appointments, name='list_appointments'),
    path('appointment.html', views.appointment_view, name='appointment'),
    path('home.html', views.home, name='home'),
    path('main.html', views.main, name='main'),
    path('blog.html', views.blog, name='blog'),
    path('contact.html', views.contact, name='contact'),
    path('gallery.html', views.gallery, name='gallery'),
    path('pricing.html', views.pricing, name='pricing'),
    path('services.html', views.services, name='services'),
    path('vet.html', views.vet, name='vet'),
    path('blogsingle.html', views.blog, name='blogsingle'),
    path('about.html', views.about, name='about'),
    path('appointments.html', views.list_appointments, name='list_appointments'),

]
