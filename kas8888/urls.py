from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home, contact   # ⬅️ أضف contact

urlpatterns = [
    # الصفحة الرئيسية
    path("", home, name="home"),

    # صفحة اتصل بنا
    path("contact/", contact, name="contact"),  # ⬅️ جديد

    # لوحة تحكم Django
    path("admin/", admin.site.urls),

    # التطبيقات
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls")),
]

# إعدادات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
