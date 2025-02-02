from django.contrib import admin
from .models import Appointment, Vet, Pets, Customers, Payment

admin.site.register(Appointment)
admin.site.register(Vet)
admin.site.register(Pets)
admin.site.register(Payment)
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'is_active', 'is_staff']
    search_fields = ['email', 'phone']

