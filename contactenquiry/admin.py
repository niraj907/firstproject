from django.contrib import admin
from .models import contactEnquiry

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','websiteLink','message')

admin.site.register(contactEnquiry, ContactAdmin)