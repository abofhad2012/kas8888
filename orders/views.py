from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def orders_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/orders_list.html', {
        'orders': orders
    })
