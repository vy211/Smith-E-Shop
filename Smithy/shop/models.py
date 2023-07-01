from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('T', 'Tools'),
    ('A', 'Agriculture'),
    ('W', 'Weapones'),
    ('U', 'Utensils'),

)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    percentage = models.IntegerField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    product_image = models.ImageField(upload_to='static/image/')

    def __str__(self):
        return self.title
    @property
    def percentage(self):
        return int(((self.selling_price - self.discounted_price) * 100)/self.selling_price)


class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.name
