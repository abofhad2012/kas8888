from django.contrib import admin
from .models import Category, Product, ProductImage


# ===============================
# صور المنتج (Inline)
# ===============================
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# ===============================
# إدارة التصنيفات
# (ضروري لظهور زر + في المنتج)
# ===============================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


# ===============================
# إدارة المنتجات
# ===============================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]
