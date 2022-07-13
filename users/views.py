from django.shortcuts import redirect, render
from .forms import RegistrationForm

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