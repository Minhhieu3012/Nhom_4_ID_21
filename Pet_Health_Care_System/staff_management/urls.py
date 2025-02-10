from django.urls import path
from .views import StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView
from . import views

urlpatterns = [
    path('staffs/', StaffListView.as_view(), name='staff_list'),
    path('staffs/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staffs/add/', StaffCreateView.as_view(), name='staff_add'),
    path('staffs/<int:pk>/edit/', StaffUpdateView.as_view(), name='staff_edit'),
   
    path('staffs/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:id>/', views.staff_detail, name='staff_detail'),
    path('schedule/', views.schedule_list, name='schedule_list'),

]