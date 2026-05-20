from django.shortcuts import render
from products.models import Product

def home(request):
    products = Product.objects.all().order_by('-created_at')[:8]
    return render(request, 'home.html', {'products': products})
