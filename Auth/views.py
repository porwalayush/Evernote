from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import todoform
from .models import TODO

# Create your views here.
def signupuser(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('home')
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
    if request.user.is_authenticated:
        w = TODO.objects.filter(user=request.user)
        r=len(w)
        return render(request, 'home.html', {'list': w,'r':r})
    else:
        return render(request, 'home.html')

def createtodo(request):
    if request.method == 'POST':
        w= request.POST
        s1= TODO()
        s1.user= request.user
        s1.Task=request.POST['Task']
        s1.Task_Description=request.POST['Task_Description']
        if "Important" in w:
            s1.Important = True
        else:
            s1.Important=False
        s1.save()
        return redirect('home')
    else:
        return render(request,'createtodo.html',{'todoform':todoform})
