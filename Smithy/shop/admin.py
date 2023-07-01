from django.contrib import admin
from . models import *

# Register your models here.
# username smithy123
# email-vy840013@gmail.com
# pass-smithy@123
from django.contrib import admin
from shop.models import Product


# @admin.register(Product)
class ProductModelAdmid(admin.ModelAdmin):
    list_display = ('id', 'title', 'discounted_price', 'selling_price', 'percentage',
                    'category', 'product_image')

admin.site.register(Product, ProductModelAdmid)

class PaymentModelAdmid(admin.ModelAdmin):
    list_display = ('name', 'amount', 'payment_id', 'paid')
admin.site.register(Payment, PaymentModelAdmid)