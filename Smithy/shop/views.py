from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def tools(request):
    return render(request, 'shop/tools.html')


def weapones(request):
    return render(request, 'shop/weapones.html')


def agriculture(request):
    return render(request, 'shop/agriculture.html')


def utensils(request):
    return render(request, 'shop/utensils.html')


def login(request):
    return render(request, 'shop/login.html')


def signup(request):
    return render(request, 'shop/signup.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(
            username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'shop/tools.html')
