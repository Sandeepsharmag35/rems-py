from django.contrib import admin
from .models import Property, CustomerMessage, SellRequest

# Register your models here.


class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "property_type",
        "price",
        "city",
        "district",
        "zip_code",
        "description",
        "status",
        "property_for",
    ]


admin.site.register(Property, PropertyAdmin)


class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "fullname",
        "phone_number",
        "email",
        "message",
        "property",
        "received_at",
    ]


admin.site.register(CustomerMessage, CustomerMessageAdmin)


class SellRequestAdmin(admin.ModelAdmin):
    list_display = [
        "property_title",
        "property_for",
    ]


admin.site.register(SellRequest, SellRequestAdmin)
