from django.db import models

# Create your models here.
from users.models import CustomUser


class VKSearchResults(models.Model):
    vk_first_name = models.CharField(max_length=30)
    vk_last_name = models.CharField(max_length=30)
    vk_profile_link = models.URLField()
    interests_fields = models.TextField(max_length=300)
    id_organization_for = models.ForeignKey(CustomUser)
