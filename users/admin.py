from django.contrib import admin
from .models import Volunteer, Organizator
from .models import CustomUser

admin.site.register(Organizator)
admin.site.register(Volunteer)
admin.site.register(CustomUser)
