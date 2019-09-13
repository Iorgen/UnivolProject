# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='univol-index'),
    path('', views.home, name='univol-home'),
    path('vacancies/', views.get_vacancies, name='vacancies'),
    url('^messages/?(?P<responder>\d+)?/?$', views.chat_view, name='chat')
]
