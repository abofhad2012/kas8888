from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'قيد المعالجة'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='المستخدم'
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='إجمالي الطلب'
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='حالة الطلب'
    )

    is_paid = models.BooleanField(
        default=False,
        verbose_name='تم الدفع'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الطلب'
    )

    class Meta:
        verbose_name = 'طلب'
        verbose_name_plural = 'الطلبات'

    def __str__(self):
        return f"طلب رقم {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='الطلب'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='المنتج'
    )

    size = models.CharField(
        max_length=10,
        verbose_name='المقاس'
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='الكمية'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='سعر القطعة'
    )

    class Meta:
        verbose_name = 'عنصر طلب'
        verbose_name_plural = 'عناصر الطلب'

    def get_subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} × {self.product}"
