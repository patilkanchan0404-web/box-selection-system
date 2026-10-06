from django.contrib import admin
from .models import Product, Box

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'length',
        'width',
        'height',
        'weight'
    )

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'length',
        'width',
        'height',
        'max_weight',
        'cost'
    )