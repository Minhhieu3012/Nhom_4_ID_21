from django.urls import path
from . import views
from .views import staff_list, staff_detail, work_schedule_list, work_shift_list

urlpatterns = [

    # Quản lý nhân viên
    path('staff/', views.staff_list, name='staff_list'),
    
    path('staff/<int:id>/', views.staff_detail, name='staff_detail'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:id>/update/', views.staff_update, name='staff_update'),
    path('staff/<int:id>/delete/', views.staff_delete, name='staff_delete'),

    # Quản lý lịch làm việc
    path('work-schedule/', views.work_schedule_list, name='work_schedule_list'),
    path('work-schedule/<int:id>/', views.work_schedule_detail, name='work_schedule_detail'),
    path('work-schedule/create/', views.work_schedule_create, name='work_schedule_create'),
    path('work-schedule/<int:id>/update/', views.work_schedule_update, name='work_schedule_update'),
    path('work-schedule/<int:id>/delete/', views.work_schedule_delete, name='work_schedule_delete'),

    # Quản lý ca làm việc
    path('work-shift/', views.work_shift_list, name='work_shift_list'),
    path('work-shift/<int:id>/', views.work_shift_detail, name='work_shift_detail'),
    path('work-shift/create/', views.work_shift_create, name='work_shift_create'),
    path('work-shift/<int:id>/update/', views.work_shift_update, name='work_shift_update'),
    path('work-shift/<int:id>/delete/', views.work_shift_delete, name='work_shift_delete'),

    path('schedule/', views.work_schedule_list, name='work_schedule_list'),
    path('shift/', views.work_shift_list, name='work_shift_list'),
]
