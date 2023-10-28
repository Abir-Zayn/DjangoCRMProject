from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'first_name', 'last_name', 'usermail', 'phone', 'city', 'state']

admin.site.register(Record, RecordAdmin)
