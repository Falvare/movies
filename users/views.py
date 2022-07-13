from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView

# Create your views here.
def register(requests):
    if requests.method == 'POST':
        form = RegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login')
    else:
        form = RegistrationForm()
    
    return render('users/register.html', context={'form':form})

class Login(LoginView):
    template_name = 'users/login.html'
    success_url = '/characters'