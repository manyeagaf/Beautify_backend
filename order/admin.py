from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress,PaymentMethod

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price', 'is_paid', 'is_delivered']
    list_editable = ['is_paid', 'is_delivered']


@admin.register(ShippingAddress)
class ShippinAddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'postal_code', 'city']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price']
    list_editable = ['quantity']

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}
    

