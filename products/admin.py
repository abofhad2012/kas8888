from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created_at']
    list_filter = ['created_at', 'category']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)