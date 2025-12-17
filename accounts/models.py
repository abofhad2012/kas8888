from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='المستخدم'
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='رقم الهاتف'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )

    class Meta:
        verbose_name = 'عميل'
        verbose_name_plural = 'العملاء'

    def __str__(self):
        return self.user.username


class Address(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name='العميل'
    )

    full_name = models.CharField(
        max_length=100,
        verbose_name='الاسم الكامل'
    )

    city = models.CharField(
        max_length=100,
        verbose_name='المدينة'
    )

    region = models.CharField(
        max_length=100,
        verbose_name='المنطقة'
    )

    street = models.CharField(
        max_length=200,
        verbose_name='الشارع'
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='الرمز البريدي'
    )

    is_default = models.BooleanField(
        default=False,
        verbose_name='العنوان الافتراضي'
    )

    class Meta:
        verbose_name = 'عنوان'
        verbose_name_plural = 'العناوين'

    def __str__(self):
        return f"{self.full_name} - {self.city}"
