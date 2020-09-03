from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signupuser(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            return HttpResponse('done')
        else:
            return HttpResponse('pasword did not match')
    else:
        return render(request, 'signup.html', {'form': UserCreationForm})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')