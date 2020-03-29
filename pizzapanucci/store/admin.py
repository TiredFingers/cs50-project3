from django.contrib import admin

from .models import FoodType, Plate, FoodAddition, Orders

admin.site.register(FoodType)
admin.site.register(Plate)
admin.site.register(FoodAddition)


class OrdersAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(Orders, OrdersAdmin)
