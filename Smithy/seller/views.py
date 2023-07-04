from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')


def products(request):
    return render(request,'products.html')

def performance(request):
    return render(request,'performance.html')

def seller_orders(request):
    return render(request,'orders.html')

def seller_profile(request):
    return render(request,'profile.html')

def help_center(request):
    return render(request,'help_center.html')