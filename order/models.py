
from email.mime import image
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.


class ShippingAddress(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '{},{},{}'.format(self.address, self.city, self.country)


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(
        ShippingAddress, on_delete=models.PROTECT)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices = ((1,'pending'),(2,'shipped'),(3,'cancelled'),(4,'delivered')),default = 1)

    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=299, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(unique=False,
                              null=False,
                              blank=False,
                              default="images/default.png",
                              help_text=("format: required, default-default.png",),)

    def __str__(self):
        return str(self.id)

class PaymentMethod(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 150)

class PaymentTranSaction(models.Model):
    order = models.OneToOneField(Order,on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10,decimal_places = 2)
    date = models.DateTimeField()
    


