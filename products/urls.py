from django.urls import path

from .views import (
    ItemListAPI,
    ItemDetailAPI,
    CategoryAPI,
)

appname = 'products'

urlpatterns = [

    # for fetching items
    path('api/items/', ItemListAPI.as_view(), name='items'),
    path('api/item/<str:title_slug>', ItemDetailAPI.as_view(), name='item-detail'),

    # for fetching catogory
    path('api/category', CategoryAPI.as_view(), name='category'),

]
