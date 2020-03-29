from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Plate(models.Model):

    name = models.CharField(max_length=100)
    small_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    big_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    type_id = models.ForeignKey(FoodType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class FoodAddition(models.Model):

    name = models.CharField(max_length=100)
    small_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    big_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    plate_id = models.ForeignKey(Plate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id_user = models.IntegerField()
    cart = models.TextField() #json presentation of cart of user
