# django imports
from django.db.models import Q

# rest_framework imports
from rest_framework import generics
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

# importing serializers
from .serializers import (
    ItemListSerializer,
    ItemDetailSerializer,
    CategoryListSerializer,
)

# importing model
from .models import (
    Item,
    Category,
)


class ItemListAPI(generics.ListAPIView):
    queryset = Item.get_published_items.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'title',
        'category__ct',
    ]
    ordering_fields = [
        'price',
    ]

    def get_queryset(self):
        q = self.request.GET.get("ct_filter")
        print(q)
        if q:
            return Item.get_published_items.filter(category__ct=q)
        return Item.get_published_items.all()


class ItemDetailAPI(generics.RetrieveAPIView):
    queryset = Item.get_published_items.all()
    serializer_class = ItemDetailSerializer
    lookup_field = "title_slug"


class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = None