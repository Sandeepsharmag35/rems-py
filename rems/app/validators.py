from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)


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
