from PIL import Image
from django.core.exceptions import ValidationError
from io import BytesIO
from django.core.files.base import ContentFile
import os, math


def validate_avatar(avatar):

    img = Image.open(avatar)
    # print("avatar :: ========================= :: ", math.floor(avatar.size / 1024))
    # print("img.size :: ========================= :: ", img.format)

    isAvatarUnder100KB = math.floor(avatar.size / 1024) <= 100
    isAvatarSquared = img.width == img.height
    # isAvatarUnder400 = img.width <= 400 and img.height <= 400
    isAvatarInValidFormat = (
        img.format == "PNG"
        or img.format == "JPEG"
        or img.format == "JPG"
        or img.format == "GIF"
    )

    if not isAvatarUnder100KB:
        raise ValidationError("Avatar must be less than or equal to 100KB.")
    elif not isAvatarSquared:
        raise ValidationError("Avatar must be squared")
    elif not isAvatarInValidFormat:
        raise ValidationError("Avatar must be a PNG or JPEG image")
