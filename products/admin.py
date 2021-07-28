from django.contrib import admin

from .models import (
    Item,
    Category,
    ItemImage,
    Cart,
    OrderItem,
    Order,
)

class InLinesImages(admin.TabularInline):
    model = ItemImage
    extra = 1
    max_num = 10


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0
    readonly_fields = (
        'user',
        'item',
        'quantity',
        'ordered',
    )
    can_delete = False

    # for making add new order not possible
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Order)
class Admin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'status',
        'total_price',
    )
    list_filter = (
        'status',
        'created_date',
    )
    inlines = [
        OrderItemInline,
    ]
    readonly_fields = (
        'order_id',
        'user',
        'created_date',
        'total_price',
    )
    search_fields = (
        'order_id',
    )

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    list_display_links = ('title',)
    readonly_fields = ('title_slug', 'date_added',)
    search_fields = ('title',)

    list_editable = ('status',)

    list_per_page = 15

    # inlines
    inlines = [
        InLinesImages,
    ]

admin.site.register(Category)