from datetime import datetime

from django.db import models

from users.models import CustomUser, Organizator


class Contribution(models.Model):
    id_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # mock
    #id_organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # mock


class Vacancy(models.Model):
    vacancy_name = models.TextField(max_length=50)
    date_range = models.TextField(max_length=21)
    description = models.TextField(max_length=5000)
    organization = models.ForeignKey(Organizator, on_delete=models.CASCADE)
    competitions_keywords = models.TextField(max_length=5000)
    event_name = models.TextField(max_length=1000)


class Responds(models.Model):
    organization_id = models.IntegerField()
    volunteer_id = models.IntegerField()
    respond_date = models.DateTimeField(default=datetime.now())

