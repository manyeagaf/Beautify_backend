from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from product.models import Product, ProductAttribute, Stock, Category, Brand, Media, ProductAttributeValue


from drf.serializers import CategorySerializer, BrandSerializer, ProductSerializer, ProductMediaSerializer, OrderItemSerializer, OrderSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from drf.pagination import StandardResultsSetPagination

class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class ProductByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class ProductsList(generics.ListCreateAPIView):
    """
    Return Sub Product by WebId
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    # def get(self, request):
    #     queryset = Product.objects.all()
    #     paginator = PageNumberPagination()
    #     paginator.page_size = 1
    #     results = paginator.paginate_queryset(queryset, request)
    #     serializer = ProductSerializer(results, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductMediaList(APIView):
    def get(self, request):
        pass


class ProductMediaDetail(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        media = Media.objects.filter(product=product)
        print(media)
        serializer = ProductMediaSerializer(Media, many=True)
        return Response(serializer.data)
