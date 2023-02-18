from django.urls import path

from .views import ShopView, ProductSingleView

app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('product-single/', ProductSingleView.as_view(), name='product-single')
]