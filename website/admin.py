from django.contrib import admin
from .models import Inquiry, CallbackRequest

admin.site.register(Inquiry)
admin.site.register(CallbackRequest)