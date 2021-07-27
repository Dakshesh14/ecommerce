import razorpay

# django imports
from django.db.models import Q
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, HttpResponse

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
    OrderItem,
    Order,
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
        print(quantity)

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
        cart.quantity = quantity
        cart.save()
        return Response({
            "message": f"{item.title} has been added to your cart!"
        }, status=HTTP_202_ACCEPTED)

@login_required(login_url="accounts:login")
def user_cart(request):
    qs = Cart.objects.filter(user=request.user).distinct()
    total_price = sum([item.item.price * item.quantity for item in qs])

    return render(request, "products/user-cart.html", {
        "qs": qs,
        "total_price": total_price,
    })


@login_required(login_url="accounts:login")
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, title_slug=slug)
    cart_qs = Cart.objects.filter(user=request.user).distinct()

    for cart_item in cart_qs.all():
        if cart_item.item == item:
            cart_item.delete()

    return HttpResponseRedirect(reverse("products:my-cart"))


@login_required(login_url="accounts:login")
def order_items(request):
    if request.method == "POST":
        user = request.user

        # creating order to add in orderitem
        order = Order.objects.create(user=user)
        # getting all the items from cart
        cart_qs = Cart.objects.filter(user=user).all()

        for cart_item in cart_qs:
            order_item = OrderItem.objects.create(
                user=user,
                item=cart_item.item,
                quantity=cart_item.quantity,
                order=order,
            )
        order.save()  # saving order so that it calculate total price

        rz_key = settings.RAZORPAY_KEY
        _srz_key = settings.RAZORPAY_SECURE_KEY
        
        client = razorpay.Client(auth=(rz_key, _srz_key))
        response = client.order.create({
            "amount": order.total_price*100,
            "currency": "INR",
        })
        order.order_id = response['id']
        order.save()
        return render(request, "products/checkout.html", {
            "order": order,
            "response": response,
        })


@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        order_id = request.POST.get("razorpay_order_id")
        order = Order.objects.get(order_id=order_id)
        order.status = 'A'
        order.save()

        return render(request, "products/success.html", {
            "qs": order,
        })
