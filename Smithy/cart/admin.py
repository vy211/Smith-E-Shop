from django.contrib import admin
from cart.models import Cart

# Register your models here.
class CartModelAdmid(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'quantity','price','total_cost')

admin.site.register(Cart, CartModelAdmid)