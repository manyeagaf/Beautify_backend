from django.urls import path
from drf.views import product_views

urlpatterns = [
    path('', product_views.ProductsList.as_view(), name='products'),
    path('category/all/', product_views.CategoryList.as_view(), name='categories'),
    path('<str:pk>/', product_views.ProductDetail.as_view(), name='product-detail'),
    path('media/<str:pk>/', product_views.ProductMediaDetail.as_view(),
         name='product-media'),
    path('category/<str:slug>/', product_views.ProductByCategory.as_view()),
    path('reviews/<str:pk>/',product_views.ReviewsList.as_view(),name = 'review'),
]
