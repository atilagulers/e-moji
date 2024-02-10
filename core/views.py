from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "core/index.html",{
        "restaurants": ["McDonald's", "Burger King", "KFC"]
    })
