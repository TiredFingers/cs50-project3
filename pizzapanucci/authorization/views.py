from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User



def login(request):

    if request.user.is_authenticated:
        from django.conf import settings
        return redirect('%s?next=%s' % (reverse('store:index'), request.path))

    if request.method == 'POST':

        from django.contrib.auth import authenticate, login

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return HttpResponseRedirect(reverse('store:index'))

        else:
            return render(request, 'authorization/result.html', {'message': 'bad credentials'})

    return render(request, 'authorization/login.html', {})


def logout(request):

    from django.contrib.auth import logout

    logout(request)
    return HttpResponseRedirect(reverse('store:index'))


def registration(request):
    context = {}

    if request.method == 'POST':

        if len(User.objects.filter(username=request.POST['username'])) > 0:

            context['message'] = 'username is busy'

            return render(request, 'authorization/result.html', context)

        else:

            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user.save()

            context['message'] = 'success registration'

            return render(request, 'authorization/result.html', context)

    return render(request, 'authorization/registration.html', {'request': request})


def restore_password(request):
    return render(request, 'authorization/restore_password.html', {})


def result(request):
    return render(request, 'authorization/result.html', {})
