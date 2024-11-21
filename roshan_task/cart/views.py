from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from products.models import Product
from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(Product, pk=product_id) 
    quantity = request.POST.get('quantity', 1)
    cart.add_product(product, int(quantity))
   
    print(cart.items())
    return redirect('products_list')