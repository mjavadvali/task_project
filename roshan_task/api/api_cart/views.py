from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from products.models import Product
from cart.cart import Cart  
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartSerializer

@api_view(['POST'])
def cart_add(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(Product, pk=product_id)
    quantity = request.data.get('quantity', 1)  
    cart.add_product(product, int(quantity))
    
    
    return Response({
        'message': 'Product added to cart successfully!', }, 
        status=status.HTTP_200_OK)

@api_view(['DELETE'])
def cart_remove(request, product_id):
    cart = Cart(request.session)
    product = get_object_or_404(pk=product_id)
    if product:
        cart.remove_product(product)
        return Response({'message': 'Product removed from cart'}, status=200)
    else:
        return Response({'message': 'Product not found in cart'}, status=404)
    
@api_view(['DELETE'])
def cart_clear(request):
    cart = Cart(request.session)
    if cart.items():
        cart.clear()
        return Response({'message': 'the cart has been cleared'}, status=200)
    else:
        return Response({'message': 'you have no items in the cart to clear it'}, status=404)


class CartItems(APIView):
    def get(self, request):
        cart = Cart(request.session)

        if not cart.cart:
            return Response({'message': 'Cart is empty'}, status=200)
        total_price = cart.total_price()
        serializer = CartSerializer(cart.items(), many=True)

        response_data = {
            'cart_items': serializer.data,
            'total_price': total_price
        }

        return Response(response_data)