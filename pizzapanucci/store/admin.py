from django.contrib import admin

from .models import FoodType, Plate, FoodAddition

admin.site.register(FoodType)
admin.site.register(Plate)
admin.site.register(FoodAddition)
