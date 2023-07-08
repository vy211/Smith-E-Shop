from django.contrib import admin
from seller.models import SellerOrder

# Register your models here.
class SellerOrderModelAdmid(admin.ModelAdmin):
    list_display = ('seller','buyer', 'product', 'quantity','order_date','status','total_amount','transaction_id','address_line','city','state','postal_code','mob')

admin.site.register(SellerOrder, SellerOrderModelAdmid)