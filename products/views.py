# django imports
from django.db.models import Q

# rest_framework imports
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_202_ACCEPTED,
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

# importing serializers
from .serializers import (
    ItemListSerializer,
    ItemDetailSerializer,
    CategoryListSerializer,
    CartSerializer,
)

# importing model
from .models import (
    Item,
    Category,
    Cart,
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


class CartToggleAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        slug = request.data.get("slug")
        quantity = request.data.get("quantity", 1)
        
        try:
            item = Item.objects.get(title_slug=slug)
        except Item.DoesNotExist:
            return Response({
                "message": "No such item exist.",
            }, status=HTTP_404_NOT_FOUND)
        cart, created = Cart.objects.get_or_create(
            user=request.user,
            item=item,
        )
        if not created:
            if not quantity:
                cart.quantity += 1
            else:
                print(quantity)
                cart.quantity = quantity
            cart.save()
            return Response({
                "message": f"Product quantity has been increased to {cart.quantity}"
            }, status=HTTP_202_ACCEPTED)

        return Response({
            "message": f"{item.title} has been added to your cart!"
        }, status=HTTP_201_CREATED)
