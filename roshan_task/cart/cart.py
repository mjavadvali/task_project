from decimal import Decimal
from products.models import Product
from django.shortcuts import get_object_or_404

CART_SESSION_ID = "cart"

class Cart:
    def __init__(self, session):
        self.session = session
        self.cart = self.session.setdefault(CART_SESSION_ID, {})

    def add_product(self, product, quantity=1):
        product_title = product.title

        try:
            quantity = int(quantity)
        except ValueError:
            raise ValueError("Quantity must be an integer.")
        
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product_title} to cart. Only {product.stock} available in stock.")

        if product_title not in self.cart:
            self.cart[product_title] = {
                "quantity": 0,
                "price": str(product.price)
            }

        if self.cart[product_title]["quantity"] == 0:
            self.cart[product_title]["quantity"] = quantity
        else:
            self.cart[product_title]["quantity"] += quantity

        self.save()

    def remove_product(self, product):
        product_title = product.title
        del self.cart[product_title]
        self.save()
        

    def clear(self):
        self.cart = self.session["cart"] = {}
        self.save()

    def save(self):
        self.session.modified = True

    def items(self):
        cart_items = []
        for item in self.cart:
            product = get_object_or_404(Product, title=item)
            cart_items.append({'product':  product, 'quantity': self.cart[item]["quantity"]})
        return cart_items

    def total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def total_quantity(self):
        return sum(item["quantity"] for item in self.cart)