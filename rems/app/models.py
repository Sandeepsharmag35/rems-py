from django.db import models
from .validators import phone_regex
from django.core.exceptions import ValidationError


# Create your models here.
def image_validations(instance, filename):
    img = instance.image  # getting the image name
    print(img)
    ext = img.name.split(".")[-1].lower()
    allowed_extensions = ["jpg", "jpeg", "png"]

    if ext in allowed_extensions:
        return f"property_images/{filename}"
    else:
        raise ValidationError(
            "Invalid file format. Only JPG, JPEG, and PNG files are allowed."
        )


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
    description = models.TextField(blank=True)

    # location
    province = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=20)
    municipality = models.CharField(max_length=20, blank=True)
    ward_no = models.CharField(max_length=5, blank=True)
    tole = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="")
    featured = models.BooleanField(default=False)

    image = models.ImageField(
        upload_to=image_validations,
        blank=False,
    )
    image_side = models.ImageField(
        upload_to=image_validations,
        blank=True,
    )
    image_extra = models.ImageField(
        upload_to=image_validations,
        blank=True,
    )
    image_extra2 = models.ImageField(
        upload_to=image_validations,
        blank=True,
    )

    def __str__(self):
        return f"{self.property_type} at {self.city}, {self.district}"


class CustomerMessage(models.Model):
    fullname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=False)
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
        ("Commercial", "Commercial"),
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
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
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
    # document image
    doc_image = models.ImageField(
        upload_to="Sell_Request/Uploads/documents", blank=True
    )

    # property images
    image_front = models.ImageField(upload_to="Sell_Request/Uploads", blank=True)
    image_side = models.ImageField(upload_to="Sell_Request/Uploads", blank=True)
    image_extra = models.ImageField(upload_to="Sell_Request/Uploads", blank=True)
    image_extra2 = models.ImageField(upload_to="Sell_Request/Uploads", blank=True)

    def __str__(self):
        return self.property_title
