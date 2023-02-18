from django.urls import path
from .views import CartView, WishlistView, ViewCartBuy, ViewCartAdd, ViewCartDel, WishlistAdd, WishlistDel

app_name = 'cart_shop'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
    path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
    path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
    path('add_wishlist/<int:product_id>', WishlistAdd.as_view(), name='wishlist_add'),
    path('wishlist_del/<int:item_id>', WishlistDel.as_view(), name='wishlist_del'),
]