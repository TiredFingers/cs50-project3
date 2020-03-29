from django.shortcuts import render, redirect, reverse

from .models import FoodType, Plate, FoodAddition, Orders


def index(request):

    return render(request, 'store/index.html', {'menu': get_menu()})


def cart(request):

    if request.user.is_authenticated:

        return render(request, 'store/cart.html', {})

    else:
        return redirect(request, reverse('authorization:login'))


def order(request):

    if request.method == 'POST':
        user = request.user
        new_order = Orders(None, user.id, request.POST['order'])
        new_order.save()
        return render(request, 'store/order_success.html')

    return redirect(request, reverse('store:index'))


def order_success(request):
    return render(request, 'store/order_success.html')


def get_menu():

    return {type.id:
                 {'name': type.name, 'plates': [
                     {'name': plate.name, 'id': plate.id, 'itself': plate,
                      'additions': [
                              addition for addition in FoodAddition.objects.filter(plate_id=plate.id)
                        ]
                      }
                     for plate in Plate.objects.filter(type_id=type.id)] }
             for type in FoodType.objects.all()}

