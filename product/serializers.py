from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    attributes = serializers.SerializerMethodField(method_name='get_attributes')
    price_with_currency = serializers.SerializerMethodField(method_name='get_price_with_currency')

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'slug',
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
