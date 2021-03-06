# accounts/views.py
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import SignupForm

# 방법1 : FBV
""" def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form' : form,
    }) """

# 방법2 : CBV
signup = CreateView.as_view(model=User, 
form_class=SignupForm,
success_url=settings.LOGIN_URL,
template_name='accounts/signup.html')    

@login_required

def profile(request):
    request.user # django.contrib.auth.models.User
    return render(request, 'accounts/profile.html')


