from this import d
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Brand(models.Model):
    slug = models.SlugField(max_length=150, unique=True,)
    name = models.CharField(max_length=200, null=True,
                            blank=True, unique=True,)
    image = models.ImageField(null=True, blank=True,)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(
        max_length=100,
    )
    slug = models.SlugField(max_length=150, unique=True,)
    is_active = models.BooleanField(
        default=False,
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute",
        on_delete=models.PROTECT,
    )
    attribute_value = models.CharField(
        max_length=255,
    )


class Product(models.Model):
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True,)
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, related_name='brand', null=True, blank=True)
    product_type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, null=True, blank=True)
    # attribute_values = models.ManyToManyField(
    #     ProductAttributeValue,
    #     related_name="product_attribute_values",
    #     through="ProductAttributeValue",
    # )
    is_active = models.BooleanField(
        default=True,
    )
    image1 = models.ImageField(unique=False,
                               null=False,
                               blank=False,
                               verbose_name=("product image1"),
                               default="images/default.png",
                               help_text=("format: required, default-default.png"),)
    image2 = models.ImageField(unique=False,
                               null=True,
                               blank=False,
                               verbose_name=("product image2"),

                               help_text=("format: required, default-default.png"),)
    image3 = models.ImageField(unique=False,
                               null=True,
                               blank=True,
                               verbose_name=("product image3"),

                               help_text=("format: required, default-default.png"),)
    image4 = models.ImageField(unique=False,
                               null=True,
                               blank=True,
                               verbose_name=("product image4"),

                               help_text=("format: required, default-default.png"),)
    retail_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, error_messages={
            "name": {
                "max_length": ("the price must be between 0 and 999.99."),
            },
        },)
    store_price = models.DecimalField(max_digits=5,  decimal_places=2, error_messages={
        "name": {
            "max_length": ("the price must be between 0 and 999.99."),
        },
    },)
    sale_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        null=True,
        blank=True,
        error_messages={
            "name": {
                "max_length": ("the price must be between 0 and 999.99."),
            },
        },
    )
    is_on_sale = models.BooleanField(default=False)
    is_digital = models.BooleanField(
        default=False,
    )
    weight = models.FloatField(max_length=10, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3, null=True, blank=True, decimal_places=1)
    number_of_reviews = models.IntegerField(default=0)
    how_to_use = models.TextField(
        max_length=500, null=True, blank=True, default='How to use product')
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    class Meta:
        ordering = (["-store_price"])

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.OneToOneField(
        Product,
        related_name="product",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    last_checked = models.DateTimeField(
        null=True,
        blank=True,
    )
    units = models.IntegerField(
        default=0,
    )
    units_sold = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return str(self.units)


class Media(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="media",
        null=True,
        blank=True,
    )
    img_url = models.ImageField(unique=False,
                                null=False,
                                blank=False,
                                verbose_name=("product image"),
                                default="images/default.png",
                                help_text=("format: required, default-default.png"),)
    alt_text = models.CharField(
        max_length=255,
    )
    is_feature = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return str(self.created_at)
