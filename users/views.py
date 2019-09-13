from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import VolunteerSignUpForm, OrganizatorSignUpForm


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

#
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         # u_form = UserUpdateForm(request.POST, instance=request.user)
#         # p_form = ProfileUpdateForm(request.POST, request.FILES,
#         #                            instance=request.user.profile)
#         # if u_form.is_valid() and p_form.is_valid():
#         #     u_form.save()
#         #     p_form.save()
#         #     messages.success(request, "Your account has been updated")
#         #     return redirect('profile')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#
#     }
#     return render(request, 'users/profile.html', context)
