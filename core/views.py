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
        "restaurants": [
            {"id": 1, "name": "McDonald's"},
            {"id": 2, "name": "Burger King"},
            {"id": 3, "name": "KFC"}
        ]
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


def restaurant_view(request, restaurant_id):
    return render(request, "core/restaurant.html", {
        "restaurant_id": restaurant_id
    })


def create_restaurant(request):
    if request.method == "POST":
        name = request.POST["name"]
        min_order = request.POST["min_order"]
        delivery_fee = request.POST["delivery_fee"]
        opening_time = request.POST["opening_time"]
        closing_time = request.POST["closing_time"]
        rating = request.POST["rating"]
        type = request.POST["type"]

        # Create new restaurant
        restaurant = Restaurant(
            name=name,
            min_order=min_order,
            delivery_fee=delivery_fee,
            opening_time=opening_time,
            closing_time=closing_time,
            rating=rating,
            type=type
        )
        restaurant.save()
        return redirect('index')
    else:
        return render(request, "core/create_restaurant.html")
