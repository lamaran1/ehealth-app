from django.contrib import admin
from .models import user_details, Profile

# Register your models here.

admin.site.register(user_details)
admin.site.register(Profile)