from django.db import models

from users.models import CustomUser


class Contribution(models.Model):
    id_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # mock
    #id_organization = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # mock
