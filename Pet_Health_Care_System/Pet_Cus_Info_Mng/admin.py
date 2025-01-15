from django.contrib import admin
from .models import Customer, Pet, MedicalRecord, Appointment
from datetime import date


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('lastName', 'firstName', 'email', 'phoneNumber', 'address', 'age', 'gender')  # Hiển thị các trường
    search_fields = ('email', 'phoneNumber', 'address')  # Tìm kiếm theo email,sdt,dia chi

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # Hàm tính tuổi để hiển thị trong Admin
    @admin.display(description='Tuổi')
    def calculated_age(self, obj):
        if obj.date_of_birth:
            today = date.today()
            return today.year - obj.date_of_birth.year - (
            (today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day)
        )
        return "Chưa xác định"

    # Cấu hình hiển thị trong Admin
    list_display = ('id', 'name', 'species', 'gender', 'calculated_age', 'health_status', 'owner',) 
    search_fields = ('name', 'species')  # Tìm kiếm theo tên, loài
    list_filter = ('species', 'gender', 'health_status',)  # Bộ lọc


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'date', 'doctor', 'remarks') 
    search_fields = ('pet__name', 'doctor')  # Tìm kiếm theo tên thú cưng hoặc tên bác sĩ
    list_filter = ('date',)  # Bộ lọc theo ngày


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'pet', 'date', 'time', 'status')
    search_fields = ('customer__name', 'pet__name')  # Tìm kiếm theo tên khách hàng hoặc thú cưng
    list_filter = ('status', 'date')  # Bộ lọc theo trạng thái và ngày