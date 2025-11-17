from django.shortcuts import render, redirect
from apps.cart.cart import Cart
from .models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.error(request, 'Your cart is empty')
        return redirect('core:home')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone', '')
        order = Order.objects.create(
            user = request.user if request.user.is_authenticated else None,
            name=name, email=email, address=address, phone=phone, total=cart.get_total_price()
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_name=item['product'].name,
                product_id=item['product'].id,
                price=item['price'],
                quantity=item['quantity']
            )

        # Clear cart
        cart.clear()

        # In production here you'd integrate payment gateway (Razorpay/Stripe) and set order.status accordingly.
        order.status = 'paid'  # assume paid for demo
        order.save()

        messages.success(request, 'Order placed successfully')
        return redirect('orders:order_success', order_id=order.id)

    return render(request, 'orders/checkout.html', {'cart': cart})

def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/order_list.html', {'orders': orders})
