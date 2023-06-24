from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('tools/', views.tools, name='tools'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('weapones/', views.weapones, name='weapones'),
    path('utensils/', views.utensils, name='utensils'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('cart/',views.cart, name='cart'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('logout', views.logout_page, name="logout"),
    path('payment', views.payment, name="payment"),
    path('profile', views.profile, name="profile"),
    path('orders', views.orders, name="orders"),
]
