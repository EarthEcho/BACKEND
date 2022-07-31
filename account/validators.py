import string
from django.core.exceptions import ValidationError

allowed_characters = set(string.ascii_letters +
                         string.digits + string.punctuation)


def validate_user_password(password):
    if (len(password) < 8):
        raise ValidationError("password is too short")
    if any(pass_char not in allowed_characters for pass_char in password):
        raise ValidationError("password contains illegal characters")

    if not any(pass_char.isdigit() for pass_char in password):
        raise ValidationError("password must have at least one number")

    if not any(pass_char.isupper() for pass_char in password):
        raise ValidationError(
            "password must have at least one uppercase letter")

    if not any(pass_char.islower() for pass_char in password):
        raise ValidationError(
            "password must have at least one lowercase letter")

    if not any(pass_char in string.punctuation for pass_char in password):
        raise ValidationError(
            "password must have at least one special character")

    return True


def validate_password(password):
    if (len(password) < 8):
        return {"status": False, "message": "password is too short"}
    if any(pass_char not in allowed_characters for pass_char in password):
        return {"status": False, "message": "password contains illegal characters"}

    if not any(pass_char.isdigit() for pass_char in password):
        return {"status": False, "message": "password must have at least one number"}

    if not any(pass_char.isupper() for pass_char in password):
        return {"status": False, "message": "password must have at least one uppercase letter"}

    if not any(pass_char.islower() for pass_char in password):
        return {"status": False, "message": "password must have at least one lowercase letter"}

    if not any(pass_char in string.punctuation for pass_char in password):
        return {"status": False, "message": "password must have at least one special character"}

    return {"status": True}
