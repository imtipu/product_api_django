from django.contrib import admin
from django import forms
from django.contrib.gis.measure import D, Distance
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
        ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = [
        'title',
        'slug',
        'created',
        'last_updated'
    ]
