from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [

    path('seller/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('performance/', views.performance, name='performance'),
    path('seller-orders/', views.seller_orders, name='seller-orders'),
    path('seller-profile/', views.seller_profile, name='seller-profile'),
    path('help-center/', views.help_center, name='help-center'),
    path('seller-delete/', views.seller_delete, name='seller-delete'),
    path('add-products/', views.add_products, name='add-products'),
    path('add/', views.add, name='add'),
]