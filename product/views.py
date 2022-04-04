from django.shortcuts import render
from .models import Product

from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view

from product import serializers
# Create your views here.

def productList(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'product/product-list.html', context)


def productDetails(request, pk):
    productObj = Product.objects.get(id=pk)
    context = {
        'product': productObj
    }
    return render(request, 'product/product-details.html', context)



# REST APIs
@api_view(['GET'])
def apiProduct(request):
    api_products = Product.objects.all()
    serializer = ProductSerializer(api_products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiProductDetails(request, pk):
    api_product = Product.objects.get(id=pk)
    serializer = ProductSerializer(api_product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def apiCreateProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def apiUpdateProduct(request, pk):
    api_product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=api_product, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def apiDeleteProduct(request, pk):
    api_product = Product.objects.get(id=pk)
    api_product.delete()
    return Response('Deleted')