from django.db import models
from django.contrib.auth.models import User
from shop.models import Product



class SellerOrder(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    # PAYMENT_CHOICES = (
    #     ('credit_card', 'Credit Card'),
    #     ('paypal', 'PayPal'),
    #     ('cash_on_delivery', 'Cash on Delivery'),
    # )

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_orders')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    address_line = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    mob = models.CharField(max_length=10)

    def __str__(self):
        return f"Order #{self.pk} - Seller: {self.seller.username}, Buyer: {self.buyer.username}, Product: {self.product.name} ({self.status})"
