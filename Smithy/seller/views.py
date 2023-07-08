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
    current_user = request.user.username
    current_user_email = request.user.email

    if request.method == "POST":
        name = request.POST.get('pname')
        price = request.POST.get('pprice')
        discount = request.POST.get('pdiscount')
        category = request.POST.get('pcategory')
        quantity = request.POST.get('pquantity')
        image_file = request.FILES.get('pimg')
        description = request.POST.get('pdescription')
        new_product = Product.objects.create(
            name=name,
            price=price,
            discount=discount,
            quantity=quantity,
            category=category,
            product_image=image_file,
            description=description,
            seller = current_user,
            seller_email= current_user_email
        )
        new_product.save()
        return redirect('/products')
    return render(request, "add_products.html")