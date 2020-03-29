from django.shortcuts import render, redirect, reverse

from .models import FoodType, Plate, FoodAddition


def index(request):

    menu = {type.id:
                 {'name': type.name, 'plates': [
                     {'name': plate.name, 'id': plate.id, 'itself': plate,
                      'additions': [
                              addition for addition in FoodAddition.objects.filter(plate_id=plate.id)
                        ]
                      }
                     for plate in Plate.objects.filter(type_id=type.id)] }
             for type in FoodType.objects.all()}

    return render(request, 'store/index.html', {'menu': menu})


def cart(request):

    if request.user.is_authenticated:

        return render(request, 'store/cart.html', {})

    else:
        return redirect(request, reverse('authorization:login'))
