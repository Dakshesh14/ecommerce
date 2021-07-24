from django.urls import path

from .views import (
    ItemListAPI,
    ItemDetailAPI,
)

appname = 'products'

urlpatterns = [
    path('api/items/', ItemListAPI.as_view(), name='items'),
    path('api/item/<str:title_slug>', ItemDetailAPI.as_view(), name='item-detail'),
]
