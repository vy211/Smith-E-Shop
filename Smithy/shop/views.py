from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from shop.models import Product
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def tools(request):
    productData = Product.objects.all()
    data = {
        'productData' : productData
    }
    return render(request, 'shop/tools.html', data)


def weapones(request):
    return render(request, 'shop/weapones.html')


def agriculture(request):
    return render(request, 'shop/agriculture.html')


def utensils(request):
    return render(request, 'shop/utensils.html')


def cart(request):
    return render(request, 'shop/cart.html')


def logIn(request):
    if request.method == "POST":
        user_name = request.POST.get('userName')
        pass_word = request.POST.get('passWord1')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Username or Password!!')
            return redirect('/login')
    return render(request, 'shop/login.html')


def logoutuser(request):
    logout(request)
    return redirect("/")


def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('/signup')
        elif password != confirm_password:
            messages.info(request, 'Passwords do not match!!')
            return redirect('/signup')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect('/login')

    return render(request, 'shop/signup.html')
