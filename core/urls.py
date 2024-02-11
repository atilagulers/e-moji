from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Authentication
    path("auth/register", views.register_view, name="register"),
    path("auth/login", views.login_view, name="login"),
    path("auth/logout", views.logout_view, name="logout"),
    # Restaurants
    path("restaurants/my", views.my_restaurants, name="my_restaurants"),
    path("restaurants/create", views.create_restaurant, name="create_restaurant"),
    path("restaurants/<int:restaurant_id>", views.restaurant_view, name="restaurants"),
    path('restaurants/<int:restaurant_id>/menu', views.menu_view, name='menu_view'),
    #path("menus/<int:menu_id>", views.menu_view, name="menus"),
]
