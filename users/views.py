from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import VolunteerSignUpForm, OrganizatorSignUpForm, VolunteerUpdateForm, OrganizatorUpdateForm
from .models import Volunteer, Organizator
# TODO login after signup
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)


def register(request):
    return render(request, 'users/registration/signup.html')


def volunteer_register(request):
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created! You are now able to log in %s.!" % username)
            return redirect('login')
    else:
        form = VolunteerSignUpForm()
    return render(request, 'users/register.html', {'form': form})


def organizator_register(request):
    if request.method == 'POST':
        form = OrganizatorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created! You are now able to log in %s.!" % username)
            return redirect('login')
    else:
        form = OrganizatorSignUpForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = VolunteerUpdateForm(request.POST, request.FILES)
        profile = Volunteer.objects.filter(user=request.user)
        if not profile:
            form = OrganizatorUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated")
            return redirect('profile')
    else:
        form = VolunteerUpdateForm()
        profile = Volunteer.objects.filter(user=request.user)
        if not profile:
            form = OrganizatorUpdateForm(request.POST, request.FILES)
    context = {
        'form': form,
    }
    return render(request, 'users/profile.html', context)
