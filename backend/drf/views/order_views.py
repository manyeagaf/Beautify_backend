from datetime import datetime
from django.http import Http404
from product.models import ProductAttributeValue, Product
from order.models import Order, OrderItem, ShippingAddress,PaymentMethod
from rest_framework.response import Response
from rest_framework.views import APIView
from drf.serializers import OrderItemSerializer, OrderSerializer,PaymentMethodSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
    order = Order.objects.get(id=pk)

    user = request.user

    try:
        if user.is_staff or user == order.user:

            serializer = OrderSerializer(order)

            return Response(serializer.data)
        else:
            return Response({'detail': 'You are not authorized to view this order'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def creatOrder(request):
    user = request.user
    data = request.data
    order_items = data['order_items']
    shipping_address = ShippingAddress.objects.create(
        address=data['shipping_address']['address'],
        postal_code=data['shipping_address']['postal_code'],
        country=data['shipping_address']['country'],
        city=data['shipping_address']['city'],
    )
    order = Order.objects.create(
        user=user,
        payment_method=data['payment_method'],
        total_price=data['total_price'],
        shipping_address=shipping_address,

    )

    for item in order_items:
        product = Product.objects.get(id=item['product'])
        order_item = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
            price=item['price'],
            image=item['image'][7:],
            name=item['name']
        )
    
    serializer = OrderSerializer(order,many = False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderToPaid(request, pk):
    order = Order.objects.get(id=pk)
    order.is_paid = True
    order.paid_at = datetime.now()
    order.save()
    return Response("Order updated to paid")


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderToDelivered(request, pk):
    order = Order.objects.get(id=pk)
    order.is_delivered = True
    order.delivered_at = datetime.now()
    order.save()
    return Response("Order updated to paid")

@api_view(['GET'])

def allPaymentMethods(request):
    payments = PaymentMethod.objects.all()
    serializer = PaymentMethodSerializer(payments,many = True)
    return Response(serializer.data)

