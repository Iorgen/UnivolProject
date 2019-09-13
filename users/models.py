from django.contrib.auth.models import User
from django.db import models

from univol.models import Contacts


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=5000, null=False)
    contacts = models.ForeignKey(Contacts)
    organization_logo = models.ImageField(verbose_name='Logo', name='Logo')
    country = models.TextField(max_length=30)
    city = models.TextField(max_length=30)
    address = models.TextField(max_length=100)


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)


