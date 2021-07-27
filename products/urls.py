from django.urls import path

from .views import (
    ItemListAPI,
    ItemDetailAPI,
    CategoryAPI,
    CartToggleAPI,
    user_cart,
    remove_from_cart,
    order_items,
    payment_success,
)

app_name = 'products'

urlpatterns = [

    # for fetching items
    path('api/items/', ItemListAPI.as_view(), name='items'),
    path('api/item/<str:title_slug>', ItemDetailAPI.as_view(), name='item-detail'),

    # for fetching catogory
    path('api/category', CategoryAPI.as_view(), name='category'),

    # for add/removing item from cart
    path('api/cart', CartToggleAPI.as_view(), name='cart'),
    path('remove/<str:slug>', remove_from_cart, name='remove-item'),

    path('my-cart', user_cart, name='my-cart'),
    path('order', order_items, name='order'),
    path('payment-complete', payment_success, name='payment-complete'),

]
