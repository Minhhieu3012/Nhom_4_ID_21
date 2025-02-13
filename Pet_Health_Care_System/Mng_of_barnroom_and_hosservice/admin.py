from django.contrib import admin
from .models import Pet, Owner, Room, Admission, Staff, Invoice
# Register your models here.
#admin.site.register(Pet)
#admin.site.register(Owner)

#admin.site.register(Room)

#admin.site.register(Admission)

#admin.site.register(Staff)

#admin.site.register(Invoice)


class PetAdmin(admin.ModelAdmin):
  list_display = ("name", "species", "breed", "gender", "birth_day", "owner")

class OwnerAdmin(admin.ModelAdmin):
  list_display = ("full_name", "phone_num", "email", "address", "gender")

class RoomAdmin(admin.ModelAdmin):
  list_display = ("room_type", "capacity", "status")

class AdmissionAdmin(admin.ModelAdmin):
  list_display = ("pet", "room", "admission_date", "discharge_date")

class StaffAdmin(admin.ModelAdmin):
  list_display = ("full_name", "role", "phone_number", "email", "hire_date", "gender")

class InvoiceAdmin(admin.ModelAdmin):
  list_display = ("admission", "issued_date", "total_amount", "is_paid", "payment_date", "notes")


admin.site.register(Pet, PetAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Invoice, InvoiceAdmin)