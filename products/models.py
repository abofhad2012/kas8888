from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='اسم التصنيف'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )

    class Meta:
        verbose_name = 'تصنيف'
        verbose_name_plural = 'التصنيفات'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='التصنيف'
    )

    name = models.CharField(
        max_length=200,
        verbose_name='اسم المنتج'
    )

    description = models.TextField(
        blank=True,
        verbose_name='وصف المنتج'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='السعر'
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name='المخزون'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإضافة'
    )

    class Meta:
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='المنتج'
    )

    # ✅ التعريف الصحيح بدون تكرار verbose_name
    image = CloudinaryField(
        verbose_name='صورة المنتج'
    )

    class Meta:
        verbose_name = 'صورة منتج'
        verbose_name_plural = 'صور المنتجات'

    def __str__(self):
        return f"صورة للمنتج {self.product.name}"
