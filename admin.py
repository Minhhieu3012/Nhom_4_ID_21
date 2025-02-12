from django.contrib import admin
from .models import User, AuditLog

admin.site.register(User)
admin.site.register(AuditLog)
