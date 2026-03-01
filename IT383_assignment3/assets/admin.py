from django.contrib import admin
from .models import Asset, MaintenanceLog

admin.site.register(Asset)
admin.site.register(MaintenanceLog)