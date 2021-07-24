# django imports
from django.db.models import Q

# rest_framework imports
from rest_framework import generics
from rest_framework.filters import SearchFilter

# importing serializers 
from .serializers import (
    ItemListSerializer,
    ItemDetailSerializer,
)

# importing model
from .models import (
    Item,
)


class ItemListAPI(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,]
    search_fields = [
        'title',
        'category__ct',
    ]


class ItemDetailAPI(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = "title_slug"