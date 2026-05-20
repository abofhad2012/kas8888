from django.contrib import admin
from django.urls import path, include
from .views import home
from .page_views import contact_view, about_view

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),

    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]