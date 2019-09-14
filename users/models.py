from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_organizator = models.BooleanField(default=False)


class Volunteer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='usr')
    first_name = models.CharField(max_length=100, null=False, default='')
    last_name = models.CharField(max_length=100, null=False, default='')
    # contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, null=False, default='')
    city = models.CharField(max_length=30, null=False, default='')
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    description = models.TextField(max_length=5000, default='')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Organizator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.TextField(max_length=100, null=False)
    description = models.TextField(max_length=5000, null=False)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    country = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=100, default='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
