import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, fullname, email, password, **extra_fields):
        if not email or not fullname or not password:
            raise ValueError("The Fullname, Email and Password field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.uniqueId = f"{fullname.replace(" ", "-").lower()}-{user.id}"
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        superuser = self.model(email=email, fullname=fullname, **extra_fields)
        superuser.set_password(password)
        superuser.uniqueId = f"{fullname.replace(" ", "-").lower()}-{superuser.id}"
        superuser.save(using=self._db)

        return superuser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="images/avatar", blank=True, default="default_avatar.png")
    email = models.EmailField(max_length=254, unique=True)
    fullname = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(unique=False, max_length=254, null=True, blank=True)
    uniqueId = models.CharField(
        max_length=9999, null=False, blank=False
    )  # user.uniqueId = f"{fullname.replace(" ", "-").lower()}-{user.id}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    objects = UserManager()
