from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import check_password



# Create your views here.

def index(request):
    return render(request, "core/index.html",{
        "restaurants": ["McDonald's", "Burger King", "KFC"]
    })


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords must match.") 
            return redirect('register')
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.set_password(password)
            user.save()
            messages.success(request, "Regis tration successful!")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Username already taken.")
            return redirect('register')
        

    return render(request, "core/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, 
        password=password)
        
        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username and/or password.")
            return redirect('login')
    else:
        return render(request, "core/login.html")

def logout_view(request):
    logout(request)
    return redirect('index')
