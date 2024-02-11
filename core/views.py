from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "core/index.html",{
        "restaurants": ["McDonald's", "Burger King", "KFC"]
    })


def register_view(request):
    return render(request, "core/register.html")

def login_view(request):
    return render(request, "core/login.html")
