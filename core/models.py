from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum

class User(AbstractUser):
    restaurants = models.ManyToManyField("Restaurant", blank=True, default=[], related_name="users")



class Restaurant(models.Model):
    class RestaurantType(Enum):
        FAST_FOOD = "Fast Food"
        CASUAL_DINING = "Casual Dining"
        FINE_DINING = "Fine Dining"
        CAFE = "Cafe"
        BAR = "Bar"
        FOOD_TRUCK = "Food Truck"
        PIZZERIA = "Pizzeria"


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
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
