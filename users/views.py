from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from movies_app.models import Movie, Character

# Create your views here.
def register(requests):
    if requests.method == 'POST':
        form = RegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login')
    else:
        form = RegistrationForm()
    
    return render(requests, 'users/register.html', context={'form':form})

class Login(LoginView):
    template_name = 'users/login.html'
    success_url = '/characters'

def profile(requests):
    user = User.objects.get(username=requests.user.username)
    return render(requests, 'users/profile.html', context={'user':user})