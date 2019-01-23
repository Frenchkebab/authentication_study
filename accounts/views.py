# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def signup(request):
    pass

@login_required
def profile(request):
    request.user # django.contrib.auth.models.User
    return render(request, 'accounts/profile.html')


