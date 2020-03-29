from django.urls import path

from . import views

app_name = 'authorization'

urlpatterns = [

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('restore_password/', views.restore_password, name='restore_password'),
    path('registration/', views.registration, name='registration'),
    path('result/', views.result, name='result')
]
