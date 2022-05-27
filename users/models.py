from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField,
    EmailField,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractUser):
    email = EmailField(_("Email Address"), unique=True, null=True, blank=True)
    mobile = CharField(
        _("Mobile Number"), max_length=16, unique=True, blank=True, null=True
    )
    first_name = models.CharField(max_length=255, verbose_name="First name")
    last_name = models.CharField(max_length=255, verbose_name="Last name")
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name or self.email or self.mobile or ""





