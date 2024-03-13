from django.shortcuts import render
from . import models
from .models import Product

# Create your views here.
def product(request):
    products= Product.objects.all()
    return render(request,'product/main.html',{'products':products})

def single(request):
    products= Product.objects.all()
    return render(request,'product/single.html',{'products':products})

