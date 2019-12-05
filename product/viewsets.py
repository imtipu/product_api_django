from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import filters as rest_filters, status

from .models import *
from .serializers import *


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny, ]

    # def post(self, reques= AttributeVariantsSerializer(data=request.data)t):
    #     variant_serializer

    def create(self, request, *args, **kwargs):
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
                    att_price = '0.00'
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

from .filtersets import *
class ProductAttributeViewSet(ModelViewSet):
    queryset = AttributeVariants.objects.all()
    serializer_class = AttributeVariantsSerializer
    filter_class = AttributeFilterSet
    filter_backends = [rest_filters.SearchFilter, DjangoFilterBackend, rest_filters.OrderingFilter, ]
    # filterset_fields = ['type', 'price', ]

    def get_queryset(self):
        return AttributeVariants.objects.filter(product=self.kwargs['products_pk'])
    # def list(self, request):
    #     attributes = AttributeVariants.objects.filter(product=request.pk)
    #     serializer = AttributeVariantsSerializer(attributes, many=True)
    #     return Response(serializer.data)

