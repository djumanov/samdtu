from django.core.exceptions import ValidationError


def validate_image_size(image):
    max_size_mb = 2 * 1024 * 1024  # Maximum size in 2 MB
    if image.size > max_size_mb:
        raise ValidationError(f"The maximum file size that can be uploaded is {max_size_mb}MB")
