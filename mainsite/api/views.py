from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Productserializer
from .models import Product
from rest_framework import serializers
from . import serializer

@api_view(['GET'])
def showall(request):
    products=Product.objects.all()
    serializer=Productserializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def choice(request,id):
    product=Product.objects.get(pk=id)
    serializer=Productserializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer=Productserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def update(request,id):
    product=Product.objects.get(pk=id)
    serializer=Productserializer(product,instance=product)
    return Response(serializer.data)

@api_view(['GET'])
def delete(request,id):
    product=Product.objects.get(pk=id)
    product.delete()
    return Response('Items delete successfully!!!')



