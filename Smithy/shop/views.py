from django.shortcuts import render
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
