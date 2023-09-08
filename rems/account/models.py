from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def image_validations(instance, filename):
    img = instance.profile_picture  # getting the image name
    ext = img.name.split(".")[-1].lower()
    allowed_extensions = ["jpg", "jpeg", "png"]

    if ext in allowed_extensions:
        return f"profile_pictures/{filename}"
    else:
        raise ValidationError(
            "Invalid file format. Only JPG, JPEG, and PNG files are allowed."
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.TextField(max_length=50, blank=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.TextField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to=image_validations, blank=True)

    def __str__(self):
        return self.fullname
