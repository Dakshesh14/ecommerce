from django.contrib import admin

from .models import (
    Item,
    Category,
    ItemImage,
    CartItem,
    Cart,
)

class InLinesImages(admin.TabularInline):
    model = ItemImage
    extra = 1
    max_num = 10


admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Cart)

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
