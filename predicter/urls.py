# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='univol-index'),
    path('', views.home, name='univol-home'),
]
