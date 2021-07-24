from django.contrib import admin

# importing models
from .models import Blog, Category


# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'date_added',)
#     list_display_links = ('title',)
#     list_editable = ('status',)

#     search_fields = ('title', 'category',)

#     readonly_fields = ('title_slug', 'date_added',)

#     list_per_page = 15


# admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_added',)
    list_display_links = ('title',)
    list_editable = ('status',)

    search_fields = ('title', 'category',)

    readonly_fields = ('title_slug', 'date_added',)

    list_per_page = 15