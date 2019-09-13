from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

# Create your views here.
# @login_required
def index(request):
    context = {
        "some_content": 'you you are here'
    }
    return render(request, 'univol/index.html', context)


def home(request):
    context = {
        "some_content": 'you you are here'
    }
    return render(request, 'univol/index.html', context)
