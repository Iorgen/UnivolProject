from django.db import models


class Contacts(models.Model):
    phone_number = models.TextField(max_length=40)
    # viber = phone_number
    # telegram = phone_number
    instagram_user_name = models.TextField(max_length=100)
    facebook_link = models.TextField(max_length=100)
    vk_link = models.TextField(max_length=100)
    email_adress = models.TextField(max_length=100)
