from django.urls import reverse
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.relations import *

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    attributes = serializers.SerializerMethodField(method_name='get_attributes')
    product_url = serializers.SerializerMethodField(method_name='get_product_url')
    price_with_currency = serializers.SerializerMethodField(method_name='get_price_with_currency')

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'slug',
            'product_url',
            'price',
            'price_with_currency',
            'currency',
            'created',
            'last_updated',
            'attributes',
        ]
        extra_kwargs = {
            'slug': {
                'read_only': True,
            }
        }


    def get_product_url(self, instance):
        return str(instance.get_absolute_url())

    def get_attributes(self, instance):
        variants = AttributeVariants.objects.filter(product=instance.id)
        serializer = AttributeVariantsSerializer(variants, many=True)
        return serializer.data

    def get_price_with_currency(self, instance):
        price = str(instance.price)
        currency = str(instance.currency)
        return str(price + ' ' + currency)


class AttributeVariantsSerializer(serializers.ModelSerializer):
    price_with_currency = serializers.SerializerMethodField(method_name='get_price_with_currency')

    class Meta:
        model = AttributeVariants
        fields = [
            'pk',
            'product',
            'type',
            'name',
            'price',
            'price_with_currency',
        ]

    def get_price_with_currency(self, instance):
        price = str(instance.price)
        currency = str(instance.product.currency)
        return str(price + ' ' + currency)
