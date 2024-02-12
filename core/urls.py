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
    path('restaurants/<int:restaurant_id>/menu/add-item', views.add_menu_item, name='add_menu_item'),
    
    # Review
    path('restaurants/<int:restaurant_id>/reviews', views.reviews_view, name='reviews_view'),
    path('restaurants/<int:restaurant_id>/reviews/create', views.add_review, name='add_review'),
]
