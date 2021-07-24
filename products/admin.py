from django.contrib import admin

from .models import (
    Item,
    Category,
)


admin.site.register(Category)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status',)
    list_display_links = ('title',)
    readonly_fields = ('title_slug', 'date_added',)
    search_fields = ('title',)

    list_editable = ('status',)

    list_per_page = 15