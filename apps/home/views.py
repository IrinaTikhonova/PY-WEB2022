from django.shortcuts import render
from django.views import View

from apps.cart_shop.models import Product, WishlistItem, CartItemShop
from apps.cart_shop.views import fill_card_in_session, fill_id_card_in_session

class IndexShopView(View):
    def get(self, request):
        fill_card_in_session(request)
        fill_id_card_in_session(request)

        data = Product.objects.all()
        wishlist = WishlistItem.objects.filter(wishlist__user=request.user)
        products = [item.product.name for item in wishlist]
        cart = CartItemShop.objects.filter(cart__user=request.user)
        products_cart = [item.product.name for item in cart]
        context = {'data': data,
                   'wishlist_items': products,
                   'cart_items': products_cart
                   }
        return render(request, 'home/index.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')