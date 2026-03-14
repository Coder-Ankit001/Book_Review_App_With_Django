from django.contrib import admin

from .models import UserProfile, ReadingStatus

admin.site.register(UserProfile)
admin.site.register(ReadingStatus)
