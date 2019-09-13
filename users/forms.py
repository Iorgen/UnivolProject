from django import forms
from .models import CustomUser, Volunteer, Organizator
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class VolunteerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, initial='')
    last_name = forms.CharField(max_length=100,  initial='')
    country = forms.CharField(max_length=100,  initial='')
    city = forms.CharField(max_length=100,  initial='')

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_volunteer = True
        user.save()
        volunteer = Volunteer.objects.create(user=user)
        volunteer.first_name = self.cleaned_data.get('first_name')
        volunteer.last_name = self.cleaned_data.get('last_name')
        volunteer.country = self.cleaned_data.get('country')
        volunteer.city = self.cleaned_data.get('city')
        return user


class OrganizatorSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organizator = True
        user.save()
        organizator = Organizator.objects.create(user=user)
        organizator.name = self.cleaned_data.get('name')
        organizator.description = self.cleaned_data.get('description')
        return user


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
#
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
