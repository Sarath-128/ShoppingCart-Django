from django.contrib import admin
from .models import UserProfile, LoginTable

admin.site.register(UserProfile)
admin.site.register(LoginTable)