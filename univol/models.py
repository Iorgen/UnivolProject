from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from users.models import CustomUser, Organizator, Volunteer


class Contribution(models.Model):
    id_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # mock
    #id_organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # mock


class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=50)
    date_range = models.DateTimeField(default=datetime.now())
    description = models.TextField(max_length=5000)
    competitions_keywords = models.CharField(max_length=500)
    event_name = models.CharField(max_length=100)
    organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=get_user_model())


class Responds(models.Model):
    organization_id = models.IntegerField()
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    respond_date = models.DateTimeField(default=timezone.now)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

