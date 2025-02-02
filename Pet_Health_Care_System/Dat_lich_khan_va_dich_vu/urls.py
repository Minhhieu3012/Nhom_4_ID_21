from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
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
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('customers/', views.list_customers, name='list_customers'),
    path('pets/', views.list_pets, name='list_pets'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
