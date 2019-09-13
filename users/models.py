from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_organizator = models.BooleanField(default=False)


class Volunteer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.TextField(max_length=100, null=False)
    last_name = models.TextField(max_length=100, null=False)
    # contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    country = models.TextField(max_length=30, null=False)
    city = models.TextField(max_length=30, null=False)
    # photo = models.ImageField(verbose_name='User photo', name='User photo')
    # rating = models.FloatField(default=0)
    # description = models.TextField(max_length=5000)
    # employment_situation = models.TextField(max_length=100)


class Organizator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=5000, null=False)
    # organization_logo = models.ImageField(verbose_name='Logo', name='Logo')
    # country = models.TextField(max_length=30)
    # city = models.TextField(max_length=30)
    # address = models.TextField(max_length=100)

#
# # ---------------------
# class Contacts(models.Model):
#     phone_number = models.TextField(max_length=40)
#     # viber = phone_number
#     # telegram = phone_number
#     instagram_user_name = models.TextField(max_length=100)
#     facebook_link = models.TextField(max_length=100)
#     vk_link = models.TextField(max_length=100)
#     email_adress = models.TextField(max_length=100)
#
#
# # from users.models import Organization
# class Organization(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     name = models.TextField(max_length=100, null=False)
#     description = models.TextField(max_length=5000, null=False)
#     contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
#     organization_logo = models.ImageField(verbose_name='Logo', name='Logo')
#     country = models.TextField(max_length=30)
#     city = models.TextField(max_length=30)
#     address = models.TextField(max_length=100)
#
#
# class Volunteer(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     first_name = models.TextField(max_length=100, null=False)
#     last_name = models.TextField(max_length=100, null=False)
#     contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
#     county = models.TextField(max_length=30, null=False)
#     city = models.TextField(max_length=30, null=False)
#     photo = models.ImageField(verbose_name='User photo', name='User photo')
#     rating = models.FloatField(default=0)
#     description = models.TextField(max_length=5000)
#     employment_situation = models.TextField(max_length=100)
#
#
# class Vacancy(models.Model):
#     vacancy_name = models.TextField(max_length=50)
#     date_range = models.TextField(max_length=21)
#     description = models.TextField(max_length=5000)
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
#     competitions_keywords = models.TextField(max_length=5000)
#     event_name = models.TextField(max_length=1000)
#
#
# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
#
#     def __str__(self):
#         return "%s Profile" % self.user.username
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
#         img = Image.open(self.image.path)
#
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)

