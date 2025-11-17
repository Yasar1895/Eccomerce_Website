from django.shortcuts import render, redirect, get_object_or_404
from apps.core.models import Product
from .cart import Cart
from django.views.decorators.http import require_POST
from django.contrib import messages

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    messages.success(request, f'Added {product.name} to cart.')
    return redirect(product.get_absolute_url())

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f'Removed {product.name}')
    return redirect('cart:cart_detail')
