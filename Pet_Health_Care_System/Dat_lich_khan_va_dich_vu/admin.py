from django.contrib import admin

from django.contrib import admin
from .models import Appointment, Vet, Pets, Customers, Payment

admin.site.register(Appointment)
admin.site.register(Vet)
admin.site.register(Pets)
admin.site.register(Customers)
admin.site.register(Payment)

