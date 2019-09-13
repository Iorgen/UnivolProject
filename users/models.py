from django.contrib.auth.models import User
from django.db import models

from univol.models import Contacts


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=5000, null=False)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    organization_logo = models.ImageField(verbose_name='Logo', name='Logo')
    country = models.TextField(max_length=30)
    city = models.TextField(max_length=30)
    address = models.TextField(max_length=100)


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=100, null=False)
    last_name = models.TextField(max_length=100, null=False)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    county = models.TextField(max_length=30, null=False)
    city = models.TextField(max_length=30, null=False)
    photo = models.ImageField(verbose_name='User photo', name='User photo')
    rating = models.FloatField(default=0)
    description = models.TextField(max_length=5000)
    employment_situation = models.TextField(max_length=100)


class Vacancy(models.Model):
    vacancy_name = models.TextField(max_length=50)
    date_range = models.TextField(max_length=21)
    description = models.TextField(max_length=5000)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    competitions_keywords = models.TextField(max_length=5000)
    event_name = models.TextField(max_length=1000)





