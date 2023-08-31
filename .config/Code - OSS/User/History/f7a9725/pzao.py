from django.shortcuts import render
from .cart import Cart

# def cart_remove(request, product_id)

def cart_detail(request):
    cart = Cart(request)
    return render(requests, 'cart/detail.html', {'cart':cart})
