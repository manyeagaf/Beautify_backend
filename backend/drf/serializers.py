
from dataclasses import dataclass
from enum import unique
from wsgiref.validate import validator
from rest_framework import serializers
from product.models import Product, ProductAttribute, Stock, Category, Brand, Media, ProductAttributeValue
from order.models import Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'isAdmin']

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.username
        return name


class UserSerializerWithToken(UserSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'isAdmin', ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'image']
        read_only = True


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        depth = 2
        exclude = ["id"]
        read_only = True


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'is_active', 'slug']
        read_only = True


class ProductMediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["id", "img_url", "alt_text", "is_feature"]
        # read_only = True
        # editable = False

    def get_img_url(self, obj):
        return obj.img_url.url


class ProductSerializer(serializers.ModelSerializer):

    media = ProductMediaSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "image1",
            "image2",
            "image3",
            "image4",
            "store_price",
            "sale_price",
            "brand",
            "is_on_sale",
            "weight",
            "media",
            'description',
            "how_to_use",
            'rating',
            'category',
            'number_of_reviews',
        ]
        read_only = True

    def get_category(self, obj):
        category = Category.objects.get(name=obj.category)
        serializer = CategorySerializer(category)
        return serializer.data

# User Serializers


class userSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'username', 'is_admin']

    def get_is_admin(self, obj):

        return obj.is_staff


# Order Serializers


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = userSerializer(many=False, read_only=True)
    shipping_address = ShippingAddressSerializer(many=False, read_only=True)
    order_items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order

        fields = ['id', 'user', 'shipping_address', 'total_price',
                  'is_paid', 'is_delivered', 'order_items']

    def get_order_items(self, obj):
        order_items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return serializer.data


# class RegisterSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username', 'email',
#                   'password',)

#         extra_kwargs = {"password": {"write_only": True}}

#     def create(self, validated_data):
#         username = validated_data['username']
#         email = validated_data['email']

#         password = validated_data['password']
#         user_obj = User(
#             username=username,
#             email=email,
#         )
#         user_obj.set_password(password)
#         user_obj.save()
#         return user_obj


# User Serializers
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
