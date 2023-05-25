from django.core.exceptions import ValidationError
import re


class SpecialCharacterAndNumberValidator:
    def validate(self, password, user=None):
        if not re.search(r'[~!@#$%^&*()_+}{":?><,./;\']', password) or not any(
            char.isdigit() for char in password
        ):
            raise ValidationError(
                "The password must contain at least one special character (~!@#$%^&*()_+}{\":?><,./;') and one number.",
                code="password_no_special_character_or_number",
            )

    def get_help_text(self):
        return "Your password must contain at least one special character (~!@#$%^&*()_+}{\":?><,./;') and one number."
