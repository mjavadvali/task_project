from .cart import Cart

def cart_processor(request):
    cart = Cart(request.session)
    total_quantity = cart.total_quantity()
    total_price = cart.total_price()
    return {"cart": cart, "total_quantity": total_quantity, "total_price": total_price}
