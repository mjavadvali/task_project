from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from products.models import Product
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import View
from django.http.response import JsonResponse

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


class CartRemoveItem(View):
    def delete(self, request, product_id):
        cart = Cart(request.session)
        product = get_object_or_404(Product, pk=product_id)
        cart.remove_product(product)
        return redirect('cart-summary')


def cart_remove(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove_product(product)
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

@require_POST
def cart_clear(request):
    cart = Cart(request.session)
    cart.clear()
    return redirect('products_list')

@require_GET
def cart_summary(request):
    cart = Cart(request.session)
    cart_items = cart.items()
    print(cart.items())
    for item in cart.items():
        print(item['quantity'])
    return render(request, 'cart/cart_summary.html', {'items': cart_items, 'total_price': cart.total_price()})