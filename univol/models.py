from django.db import models

from users.models import Organization


class Contacts(models.Model):
    phone_number = models.TextField(max_length=40)
    viber = phone_number
    telegram = phone_number
    instagram_user_name = models.TextField(max_length=100)
    facebook_link = models.TextField(max_length=100)
    vk_link = models.TextField(max_length=100)
    email_adress = models.TextField(max_length=100)


class Vacancy(models.Model):
    vacancy_name = models.TextField(max_length=50)
    date_range = models.TextField(max_length=21)
    description = models.TextField(max_length=5000)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    competitions_keywords = models.TextField(max_length=5000)
    event_name = models.TextField(max_length=1000)
