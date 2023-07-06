from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from shop.models import Product
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')


def products(request):
    productData = Product.objects.all()
    data = {
        'productData': productData
    }
    return render(request,'products.html',data)

def performance(request):
    return render(request,'performance.html')

def seller_orders(request):
    return render(request,'orders.html')

def seller_profile(request):
    return render(request,'profile.html')

def help_center(request):
    return render(request,'help_center.html')

def seller_delete(request):
    product_id = request.GET.get('product_id')
    Product.objects.filter(id=product_id).delete()
    messages.success(request, "Your item deleted from cart !!")
    return redirect('/products')

def add_products(request):
    return render(request,'add_products.html')



def add(request):
   
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        new_product = Product.objects.create(
            name=name,
            price=price,
            discount=discount,
            quantity=quantity,
            image=image,
            description=description
        )
        new_product.save()
    return redirect('/add-products')