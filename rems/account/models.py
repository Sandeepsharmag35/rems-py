from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.TextField(max_length=50, blank=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # max_length should be enough to accommodate the longest possible phone number, with the country code
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.user
