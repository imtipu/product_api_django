from django.shortcuts import render

# Create your views here.

# api views
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *

from .models import *
from .serializers import *


class AddProduct(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):

        # print(user)
        # print(request.data)
        data = request.data
        product_price = '0.00'
        if data.get('price'):
            product_price = data.get('price')
        product_serializer = ProductSerializer(data={
            'title': data.get('title'),
            'price': product_price,
            'currency': data.get('currency'),
        })
        if product_serializer.is_valid(raise_exception=True):
            product_data = product_serializer.save()
            if data.get('attributes'):
                for att in data.get('attributes'):
                    att_type = att['type']
                    att_name = att['name']
                    att_price = ''
                    if att['price'] != "":
                        att_price = att['price']
                    else:
                        att_price = product_price
                    print(type)
                    attribute_serializer = AttributeVariantsSerializer(data={
                        'product': product_data.id,
                        'type': att_type,
                        'name': att_name,
                        'price': att_price,
                    })
                    if attribute_serializer.is_valid(raise_exception=True):
                        attribute_serializer.save()
                return Response(data=product_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny, ]

class ProductDetails(APIView):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductAttributes(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]
    def get(self, request, pk):
        attributes = AttributeVariants.objects.filter(product=pk)
        serializer = AttributeVariantsSerializer(attributes, many=True)
        return Response(serializer.data)


class ProductUpdate(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]

    def patch(self, request, pk):
        data = request.data
        # return Response(data)
        qs = Product.objects.get(pk=pk)
        print(pk)
        serializer = ProductSerializer(qs, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttributeUpdate(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]

    def patch(self, request, pk):
        data = request.data
        # return Response(data)
        qs = AttributeVariants.objects.get(pk=pk)
        print(pk)
        serializer = AttributeVariantsSerializer(qs, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


