from django.db import models


# Create your models here.
class Property(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("rented", "Rented"),
        ("sold", "Sold"),
    ]
    TYPE_CHOICES = [
        ("house", "House"),
        ("land", "Land"),
    ]

    property_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="select"
    )

    city = models.CharField(max_length=100)
    Province = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="available"
    )

    def __str__(self):
        return f"{self.property_type} at {self.address}, {self.city}"
