from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import User, Restaurant, Menu, MenuItem, Review



# Create your views here.

def index(request):
    restaurants = Restaurant.objects.all()

    return render(request, "core/index.html",{
        "restaurants": restaurants
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
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menu = restaurant.menu

    return render(request, "core/restaurant.html", {
        "restaurant": restaurant,
        "menu": menu
    })


def create_restaurant(request):
    if request.method == "POST":
        name = request.POST["name"]
        min_order = request.POST["min_order"]
        delivery_fee = request.POST["delivery_fee"]
        opening_time = request.POST["opening_time"]
        closing_time = request.POST["closing_time"]
        type = request.POST["type"]

        # Create new restaurant
        restaurant = Restaurant(
            name=name,
            min_order=min_order,
            delivery_fee=delivery_fee,
            opening_time=opening_time,
            closing_time=closing_time,
            type=type
        )
        restaurant.save()
        restaurant.owners.add(request.user)
        return redirect('index')
    else:
        types = [(choice.value) for choice in Restaurant.RestaurantType]
        
        return render(request, "core/create_restaurant.html", {
            "types": types
        })

def my_restaurants(request):
    restaurants = Restaurant.objects.filter(owners=request.user)
    return render(request, "core/my_restaurants.html", {
        "restaurants": restaurants
    })



# Menu
def menu_view(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)

    menu_exists = Menu.objects.filter(restaurant=restaurant).exists()
    if not menu_exists:
        menu = Menu(restaurant=restaurant)
        menu.save()
    else:
        menu = Menu.objects.get(restaurant=restaurant)

    return render(request, "core/menu.html", {
        "restaurant": restaurant,
        "menu": menu
    })
    

def create_menu(request, restaurant_id):
    if request.method == "POST":
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        menu = Menu(restaurant=restaurant)
        menu.save()
        return redirect('my_restaurants')
    else:
        return render(request, "core/create_menu.html", {
            "restaurant_id": restaurant_id
        })

def add_menu_item(request, restaurant_id):
    if request.method == "POST":
        menu = Menu.objects.get(restaurant_id=restaurant_id)
        name = request.POST["name"]
        price = request.POST["price"]
        description = request.POST["description"]
        item = MenuItem(
            menu=menu,
            name=name,
            price=price,
            description=description
        )
        item.save()
        print(item)
        return redirect('menu_view', restaurant_id=restaurant_id)
    else:
        return redirect('menu_view', restaurant_id=restaurant_id)
    

def reviews_view(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    reviews = Review.objects.filter(restaurant=restaurant)
    
    return render(request, "core/reviews.html", {
        "restaurant": restaurant,
        "reviews": reviews
    })

def add_review(request, restaurant_id):
    if request.method == "POST":
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        rating = request.POST["rating"]
        comment = request.POST["comment"]
        review = Review(
            user=request.user,
            restaurant=restaurant,
            rating=rating,
            comment=comment
        )
        review.save()
    return redirect('reviews_view', restaurant_id=restaurant_id)
   
