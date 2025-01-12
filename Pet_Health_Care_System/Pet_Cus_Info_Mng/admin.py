from django.contrib import admin
from .models import Customer, Pet

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'address', 'gender')  # Hien thi cac truong
    search_fields = ('name', 'phone_number')  # Tim kiem theo ten, sdt

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'species', 'gender', 'age', 'health_status', 'owner') 
    search_fields = ('name', 'species')  # Tim kiem theo ten, loai
    list_filter = ('species', 'gender', 'health_status')  # Bo loc
