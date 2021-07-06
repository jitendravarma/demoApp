from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class BaseUserProfile(AbstractUser):
    """
    BaseUserProfile inherited from abstract user, use this model to create
    profiles
    """
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Base User Profile"
        verbose_name_plural = "Base User Profiles"

    @property
    def full_name(self):
        if self.last_name and self.first_name:
            return "%s %s" % (self.first_name, self.last_name)
        elif self.first_name:
            return "%s " % (self.first_name)
        else:
            return "%s " % (self.email)


class Text(models.Model):
    """
    This model is used to store text related datas
    """
    user_id = models.IntegerField(blank=True, null=True)
    data_id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Text"
        verbose_name_plural = "Texts"
