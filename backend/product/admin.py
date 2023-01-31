from django.contrib import admin

# Register your models here.
from .models import Product, ProductAttribute, Category, Stock, Brand, Media, ProductAttributeValue, ProductType,Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'store_price', 'brand', 'category', 'product_type']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['comment','rating']


admin.site.register(ProductAttribute)
admin.site.register(Stock)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductType)
