# api/views.py
from rest_framework import generics

from univol import models
from . import serializers


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer
