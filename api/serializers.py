from rest_framework import serializers
from univol import models


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'phone_number',
        )
        model = models.Contacts
