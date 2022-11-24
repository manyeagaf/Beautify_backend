from django.urls import path
from drf.views import order_views

urlpatterns = [

     path('', order_views.getOrders,
          name='orders-list'),
     path('myorders/', order_views.getMyOrders, name='myorders'),
     path('create/', order_views.creatOrder, name='order-create'),
     path('<str:pk>/', order_views.getOrderById, name='order'),
     path('<str:pk>/pay/', order_views.updateOrderToPaid, name="order-paid"),
     path('<str:pk>/deliver/', order_views.updateOrderToDelivered,
          name="order-delivered"),
     path('payment-methods/all/',order_views.allPaymentMethods,name = 'all-payments-methods'),

]
