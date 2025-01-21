from django.contrib import admin
from .models import Customer, Pet, MedicalRecord, Appointment, Transaction

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'email', 'phoneNumber', 'address', 'age', 'gender')  # Hiển thị các trường
    search_fields = ('email', 'phoneNumber', 'address')  # Tìm kiếm theo email,sdt,dia chi

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # Cấu hình hiển thị trong Admin
    list_display = ('id', 'name', 'species', 'gender', 'dateOfBirth', 'calculatedAge', 'healthStatus', 'owner',) 
    search_fields = ('name', 'species')  # Tìm kiếm theo tên, loài
    list_filter = ('species', 'gender', 'healthStatus',)  # Bộ lọc


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'date', 'doctor', 'remarks') 
    search_fields = ('petName', 'doctor')  # Tìm kiếm theo tên thú cưng hoặc tên bác sĩ
    list_filter = ('date',)  # Bộ lọc theo ngày


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'pet', 'date', 'time', 'status')
    search_fields = ('customerName', 'petName')  # Tìm kiếm theo tên khách hàng hoặc thú cưng
    list_filter = ('status', 'date')  # Bộ lọc theo trạng thái và ngày


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'pet', 'service', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__name', 'pet__name', 'service')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
