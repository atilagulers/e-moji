from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Authentication
    path("auth/register", views.register_view, name="register"),
    path("auth/login", views.login_view, name="login"),
    path("auth/logout", views.logout_view, name="logout"),
    # Restaurants
    path("restaurants/create", views.create_restaurant, name="create_restaurant"),
    path("restaurants/<int:restaurant_id>", views.restaurant_view, name="restaurants"),
]
