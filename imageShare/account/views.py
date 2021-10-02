from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            contact_data = form.cleaned_data
            user = authenticate(
                request, username=contact_data['username'], password=contact_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'account/login.html', context)


def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
