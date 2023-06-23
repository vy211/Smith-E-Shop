from django.shortcuts import render, redirect
from django.http import response,HttpResponse
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


def login_page(request):
    user_name=''
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('shop:index')
        else:
            return HttpResponse("Invalid input");

    return render(request, "shop/login_page.html",{'uname':user_name})


def signup_page(request):
    x=""
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(uname,email,password1,password2)
        if password1 != password2:
            x="Password not match !!"
            return render(request,"shop/signup_page.html",{'output':x})
        else:
            print(uname,email,password1,password2)
            new_user=User.objects.create_user(uname,email,password1)
            new_user.save()
            return redirect('shop:login')
    return render(request,"shop/signup_page.html")

def logout_page(request):
    logout(request)
    return redirect('/')