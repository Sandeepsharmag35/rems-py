from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "fullname", "phone_number", "address"]


admin.site.register(Profile, ProfileAdmin)
