from django.shortcuts import render, redirect, get_object_or_404
from django.http import response,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from shop.models import Product, Payment
from cart.models import *
from django.contrib.auth.decorators import login_required
import razorpay

# @login_required(login_url='shop:login')
# Create your views here.

# @login_required(login_url='shop:login')
def index(request):
    productData = Product.objects.all().exclude()[:10]
    data = {
        'productData' : productData
    }
    return render(request, 'shop/index.html', data)

# @login_required(login_url='shop:login')
def tools(request):
    productData = Product.objects.filter(category='T')
    # productData = Product.objects.all()
    data = {
        'productData' : productData
    }
    return render(request, 'shop/tools.html', data)

# @login_required(login_url='shop:login')
def weapones(request):
    productData = Product.objects.filter(category='W')
    # productData = Product.objects.all()
    data = {
        'productData' : productData
    }
    return render(request, 'shop/weapones.html', data)

# @login_required(login_url='shop:login')
def agriculture(request):
    productData = Product.objects.filter(category='A')
    # productData = Product.objects.all()
    data = {
        'productData' : productData
    }
    return render(request, 'shop/agriculture.html', data)

# @login_required(login_url='shop:login')
def utensils(request):
    productData = Product.objects.filter(category='U')
    # productData = Product.objects.all()
    data = {
        'productData' : productData
    }
    return render(request, 'shop/utensils.html', data)
# @login_required(login_url='shop:login')
def cart(request):
    cartData = Cart.objects.all()
    data = {
        'cartData': cartData
    }
    return render(request, 'shop/cart.html', data)

def success(request):
    return render(request, 'shop/payment_page.html')


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


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    if Cart.objects.filter(user=user, product=product).exists():
        return redirect('/cart')
    Cart(user=user, product=product).save()
    return redirect('/cart')



def pay_now(request):
    user=request.user 
    cart= Cart.objects.filter(user=user)
    amount = 0
    shiping_amount = 40
    l= len(cart)
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + shiping_amount
    name = request.user
    amount = totalamount
    client = razorpay.Client(auth=("rzp_test_bWZe5HkNf0YSKY", "igcgehbcVvTyxih0oPf2k9Q3"))
    payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    print(payment)
    pay = Payment(name=name, amount = amount, payment_id = payment['id'])
    pay.save()
    return render(request,'shop/payment_page.html',locals())

def show_cart(request):
    user=request.user 
    cart= Cart.objects.filter(user=user)
    amount = 0
    shiping_amount = 40
    l= len(cart)
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + shiping_amount
    #name = request.user
    #amount = totalamount
    #client = razorpay.Client(auth=("rzp_test_bWZe5HkNf0YSKY", "igcgehbcVvTyxih0oPf2k9Q3"))
    #payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    #print(payment)
    #pay = Payment(name=name, amount = amount, payment_id = payment['id'])
    #pay.save()
    return render(request,'shop/cart.html',locals())


def delete_from_cart(request):
   product_id=request.GET.get('product_id')
   Cart.objects.filter(id=product_id).delete()
   messages.success(request,"Your item deleted from cart !!")
   return HttpResponseRedirect('/cart')



def increase_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('/cart')


def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('/cart')

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    similar_products = Product.objects.filter(
        category=product.category).exclude(id=product.id)[:4]

    context = {
        'product_details': product,
        'similar_products': similar_products,
    }

    return render(request, 'shop/product_details.html', context)
