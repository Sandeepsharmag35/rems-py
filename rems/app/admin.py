from django.contrib import admin
from .models import Property, RentProperty, CustomerMessage

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
    ]


admin.site.register(Property, PropertyAdmin)


class RentPropertyAdmin(admin.ModelAdmin):
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
    ]


admin.site.register(RentProperty, RentPropertyAdmin)


class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ["id", "fullname", "phone_number", "email", "message"]


admin.site.register(CustomerMessage, CustomerMessageAdmin)
