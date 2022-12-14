from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('tools/', views.tools, name='tools'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('weapones/', views.weapones, name='weapones'),
    path('utensils/', views.utensils, name='utensils'),
    path('login/', views.logIn, name='login'),
    path('signup/', views.signUp, name='signup'),
    path('cart/',views.cart, name='cart'),
    path('logout', views.logoutuser, name="logout"),
]
