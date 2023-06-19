from django.contrib import admin
from . models import Product

# Register your models here.
# username smithy123
# email-vy840013@gmail.com
# pass-smithy@123
from django.contrib import admin
from shop.models import Product


@admin.register(Product)
class ProductModelAdmid(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'selling_price',
                    'category', 'product_image']

#admin.site.register(Product, ProductModelAdmid)