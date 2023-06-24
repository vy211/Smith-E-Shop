from django.shortcuts import render, redirect
from django.http import response,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from shop.models import Product

from django.contrib.auth.decorators import login_required


# @login_required(login_url='shop:login')
# Create your views here.

# @login_required(login_url='shop:login')
def index(request):
    return render(request, 'shop/index.html')

# @login_required(login_url='shop:login')
def tools(request):
    productData = Product.objects.all()
    data = {
        'productData' : productData
    }
    return render(request, 'shop/tools.html', data)

# @login_required(login_url='shop:login')
def weapones(request):
    return render(request, 'shop/weapones.html')

# @login_required(login_url='shop:login')
def agriculture(request):
    return render(request, 'shop/agriculture.html')

# @login_required(login_url='shop:login')
def utensils(request):
    return render(request, 'shop/utensils.html')

# @login_required(login_url='shop:login')
def cart(request):
    return render(request, 'shop/cart.html')


# @login_required(login_url='shop:login')
def wishlist(request):
    return render(request, 'shop/wishlist.html')

@login_required(login_url='shop:login')
def payment(request):
    return render(request, 'shop/payment_page.html')

@login_required(login_url='shop:login')
def profile(request):
    return render(request, 'shop/profile_page.html')

@login_required(login_url='shop:login')
def orders(request):
    return render(request, 'shop/orders_page.html')



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