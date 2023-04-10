from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views.decorators.http import require_POST


# Create your views here.
def HomePageView(request):
    # check to see if logged in user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # To authenticate
        user = authenticate(request, username=username, password =password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Hello {username}!')
            return redirect('home')
        else:
            messages.info(request, 'login failed! Please try again...')            
    return render(request, 'home.html', {})

def LoginPageView(request):
    return render(request, 'login.html', {})



def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')