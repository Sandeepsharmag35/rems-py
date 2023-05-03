from django.contrib import admin
from .models import Property, RentProperty

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display=['id', 'image', 'property_type', 'price', 'city', 'district', 'zip_code', 'description', 'status']

admin.site.register(Property, PropertyAdmin)

class RentPropertyAdmin(admin.ModelAdmin):
    list_display=['id', 'image', 'property_type', 'price', 'city', 'district', 'zip_code', 'description', 'status']

admin.site.register(RentProperty, RentPropertyAdmin)