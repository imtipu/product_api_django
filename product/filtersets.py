from django_filters import rest_framework as filters
from .models import *


class AttributeFilterSet(filters.FilterSet):
    class Meta:
        model = AttributeVariants
        fields = {
            'type': ['exact', 'in', 'startswith'],
            'price': ['exact', 'lt', 'gt', 'in', 'startswith']
        }
