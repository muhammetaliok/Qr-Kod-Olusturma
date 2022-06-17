from django.contrib import admin

from QrCodeApp.apps import QrCodeAppConfig
from QrCodeApp.models import QrCode



# Register your models here.
admin.site.register(QrCode)

