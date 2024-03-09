from django.shortcuts import render
from . import models
from .models import Product

# Create your views here.
def product(request):
    products= Product.objects.all()
    print (products)

    return render(request,'product/index.html',{'products':products})
