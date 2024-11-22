from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from products.models import Product
from django.views.decorators.http import require_POST, require_GET

@require_POST
def cart_add(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(Product, pk=product_id) 
    quantity = request.POST.get('quantity', 1)
    cart.add_product(product, int(quantity))
   
    referer_url = request.META.get('HTTP_REFERER', '/')
    print('---sssssssssss-----')
    print(cart.items())

    return redirect(referer_url)



@require_POST
def cart_remove(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove_product(product)
    return redirect('products_list')

@require_POST
def cart_clear(request):
    cart = Cart(request.session)
    cart.clear()
    return redirect('products_list')

@require_GET
def cart_summary(request):
    cart = Cart(request.session)
    cart_items = cart.items()
    print(cart_items)
    return render(request, 'cart/cart_summary.html', {'items': cart_items})