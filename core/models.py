from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum

class User(AbstractUser):
    pass


RESTAURANT_TYPE_IMAGES = {
    'Fast Food': 'fast_food.avif',
    'Cafe': 'cafe.avif',
    'Bar': 'bar.jpeg',
    'Pizzeria': 'pizzeria.jpeg',
}


class Restaurant(models.Model):
    class RestaurantType(Enum):
        FAST_FOOD = "Fast Food"
        CASUAL_DINING = "Casual Dining"
        FINE_DINING = "Fine Dining"
        CAFE = "Cafe"
        BAR = "Bar"
        FOOD_TRUCK = "Food Truck"
        PIZZERIA = "Pizzeria"

    owners = models.ManyToManyField(User, related_name="restaurants")
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100,
        choices= [(choice.name, choice.value) for choice in RestaurantType], 
        default=RestaurantType.FAST_FOOD
    )
    min_order = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    delivery_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_image_url(self):
        return RESTAURANT_TYPE_IMAGES.get(self.type)
    
    def get_avg_rating(self):
        reviews = self.reviews.all()
        if len(reviews) == 0:
            return 0
        return round(sum([review.rating for review in reviews]) / len(reviews), 2)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name="menu")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Menu for {self.restaurant.name}"
    

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.menu.restaurant.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} reviewed {self.restaurant.name} with a {self.rating} star rating"
