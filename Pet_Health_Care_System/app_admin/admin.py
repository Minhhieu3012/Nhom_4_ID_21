from django.contrib import admin
from .models import Pet, Owner, Room, Admission, Staff, Invoice
# Register your models here.
admin.site.register(Pet, Owner, Room, Admission, Staff, Invoice)