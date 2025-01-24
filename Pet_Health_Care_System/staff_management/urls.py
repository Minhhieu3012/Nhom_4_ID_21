from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:staff_id>/schedule/', views.staff_schedule, name='staff_schedule'),
]
