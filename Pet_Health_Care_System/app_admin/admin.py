from django.contrib import admin
from .models import Pet, Owner, Room, Admission, Staff, Invoice
# Register your models here.
admin.site.register(Pet)
admin.site.register(Owner)
admin.site.register(Room)
admin.site.register(Admission)
admin.site.register(Staff)
admin.site.register(Invoice)