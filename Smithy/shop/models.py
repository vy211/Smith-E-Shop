from django.db import models

# Create your models here.

# CATEGORY_CHOICES = (
#     ('T', 'Tools'),
#     ('A', 'Agriculture'),
#     ('W', 'Weapones'),
#     ('U', 'Utensils'),

# )



class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    discount = models.IntegerField(default=0)
    discounted_price = models.FloatField(default=0)
    description = models.TextField(blank= True, null=True, unique = True)
    category = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='static/image/')
    quantity=models.IntegerField(default=1)
    seller = models.CharField(default='NA',max_length=100)
    seller_email = models.CharField(default='NA',max_length=100)

    def __str__(self):
        return self.name
    @property
    def discounted_price(self):
        discount_amount = (self.price * self.discount) / 100
        discounted_price = self.price - discount_amount
        return discounted_price


class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.name
