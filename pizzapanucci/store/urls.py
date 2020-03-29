from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [

    path('', views.index, name='index'),
    path('cart/', views.cart, name='index'),
]
