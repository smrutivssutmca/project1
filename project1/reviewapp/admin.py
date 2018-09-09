from django.contrib import admin
from .models import checkin

class checkinAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'longitude', 'latitude', 'place', 'review')

admin.site.register(checkin)