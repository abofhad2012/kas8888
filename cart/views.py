from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from decimal import Decimal


def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = Decimal('0')

    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)

        quantity = item.get('quantity', 1)
        price = product.price
        subtotal = price * quantity
        total += subtotal

        image = product.images.first()

        items.append({
            'product': product,
            'image': image,
            'size': item.get('size'),
            'quantity': quantity,
            'price': price,
            'subtotal': subtotal,
        })

    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })


def add_to_cart(request, product_id):
    if request.method != 'POST':
        return redirect('/')

    product = get_object_or_404(Product, id=product_id)
    size = request.POST.get('size')

    if not size:
        return redirect(product.get_absolute_url())

    cart = request.session.get('cart', {})
    product_key = str(product_id)

    if product_key in cart:
        cart[product_key]['quantity'] += 1
    else:
        cart[product_key] = {
            'size': size,
            'quantity': 1
        }

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_key = str(product_id)

    if product_key in cart:
        del cart[product_key]
        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart:cart')


def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('cart:cart')
