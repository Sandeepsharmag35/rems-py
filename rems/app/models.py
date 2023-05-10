from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


def image_validations(instance, filename):
    img = instance.image  # getting the image name
    print(img)
    ext = img.name.split(".")[-1]
    print(ext)

    if ext.lower() == "jpg" or ext.lower() == "png" or ext.lower() == "jpeg":
        return filename
    else:
        return "error"


class Property(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("rented", "Rented"),
        ("sold", "Sold"),
    ]
    TYPE_CHOICES = [
        ("house", "House"),
        ("land", "Land"),
        ("apartment", "Apartment"),
    ]

    property_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="select"
    )
    image = models.ImageField(blank=True, upload_to=image_validations)
    price = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="available"
    )

    def __str__(self):
        return f"{self.property_type} at {self.city}, {self.district}"


class RentProperty(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("rented", "Rented"),
    ]
    TYPE_CHOICES = [
        ("house", "House"),
        ("land", "Land"),
        ("apartment", "Apartment"),
        ("flat", "Flat"),
        ("Office", "office"),
    ]

    property_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="select"
    )
    image = models.ImageField(blank=True, upload_to=image_validations)
    price = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="available"
    )

    def __str__(self):
        return f"{self.property_type} at {self.city}, {self.district}"


class CustomerMessage(models.Model):
    fullname = models.TextField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # max_length should be enough to accommodate the longest possible phone number, with the country code
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"Message from {self.fullname}."
