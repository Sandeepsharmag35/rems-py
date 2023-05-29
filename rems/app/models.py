from django.db import models
from .validators import phone_regex, image_validations

# Create your models here.


class Property(models.Model):
    STATUS_CHOICES = [
        ("Select", "Select"),
        ("Available", "Available"),
        ("Rented", "Rented"),
        ("Sold", "Sold"),
    ]
    TYPE_CHOICES = [
        ("House", "House"),
        ("Land", "Land"),
        ("Apartment", "Apartment"),
        ("Commercial", "Commercial"),
    ]
    FOR_CHOICES = [
        ("Buyer", "Buyer"),
        ("Renter", "Renter"),
    ]

    property_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="select"
    )
    property_for = models.CharField(
        max_length=20, choices=FOR_CHOICES, default="select"
    )
    image = models.ImageField(
        blank=True, validators=[image_validations], upload_to="property_images"
    )
    price = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Select")

    def __str__(self):
        return f"{self.property_type} at {self.city}, {self.district}"


class CustomerMessage(models.Model):
    fullname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    message = models.TextField(max_length=200, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.fullname}."


class SellRequest(models.Model):
    TYPE_CHOICES = [
        ("House", "House"),
        ("Land", "Land"),
        ("Apartment", "Apartment"),
        ("Commercial Property", "Commercial Property"),
    ]

    FOR_CHOICES = [
        ("Sale", "Sale"),
        ("Rent", "Rent"),
    ]
    property_title = models.CharField(max_length=255, blank=False)
    property_type = models.CharField(
        max_length=30, choices=TYPE_CHOICES, default="select"
    )
    property_for = models.CharField(
        max_length=25, choices=FOR_CHOICES, default="select"
    )
    flat_number = models.CharField(max_length=5, blank=True)
    bedrooms = models.CharField(max_length=5, blank=True)
    bathrooms = models.CharField(max_length=5, blank=True)
    living_rooms = models.CharField(max_length=5, blank=True)
    kitchens = models.CharField(max_length=5, blank=True)
    total_rooms = models.CharField(max_length=5, blank=True)
    parking = models.CharField(max_length=15, blank=True)
    built_year = models.CharField(max_length=5, blank=True)
    built_area = models.CharField(max_length=20, blank=True)
    road_size = models.CharField(max_length=20, blank=True)
    land_area = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=20, blank=True)
    facing_direction = models.CharField(max_length=20, blank=True)
    price = models.CharField(max_length=20, blank=True)
    price_per_unit = models.CharField(max_length=15, blank=True)
    full_description = models.TextField(blank=True)

    # location
    province = models.CharField(max_length=15, blank=True)
    district = models.CharField(max_length=20, blank=True)
    municipality = models.CharField(max_length=20, blank=True)
    ward_no = models.CharField(max_length=5, blank=True)
    tole = models.CharField(max_length=30, blank=True)

    # contact
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=False
    )

    def __str__(self):
        return self.property_title


class UploadedImage(models.Model):
    sell_request = models.ForeignKey(
        SellRequest, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="Sell_Request/Uploads/")

    def __str__(self):
        return self.image.name
