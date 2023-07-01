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
    path('wishlist/',views.wishlist, name='wishlist'),
    path('logout/', views.logout_page, name="logout"),
    path('payment/', views.pay_now, name="payment"),
    path('profile/', views.profile, name="profile"),
    path('orders/', views.orders, name="orders"),

    
    path('product-details/<product_id>',views.product_details,name='product_details'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('delete-from-cart/',views.delete_from_cart,name='delete-from-cart'),
    path('increase_quantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    

]
