from django.shortcuts import render
from product.models import Product
# Create your views here.

def home(request):
	products = Product.objects.all()
	print(products)
	return render(request,'home/home.html',{'products':products})
