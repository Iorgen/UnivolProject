# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='univol-home'),
    path('vacancies/', views.get_vacancies, name='univol-vacancies'),
    path('add_vacancy/', views.add_vacancy, name='univol-add-vacancy'),
    url('^responds/', views.responds_view, name='univol-responds'),
    url('^responds/?(?P<responder>\d+)?/?$', views.responds_view, name='univol-responds')
]
