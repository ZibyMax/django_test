from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductInfo


def index(request):
    products = Product.objects.all()
    for product in products:
        print(product.get_info())
    return HttpResponse()

