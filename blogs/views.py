# django imports
from django.db.models import Q

# rest_framework imports
from rest_framework import generics
from rest_framework.filters import SearchFilter


# importing pagination
from .pagination import BlogPageNumberPagination

# importing serializers 
from .serializers import (
    BlogSerializer,
    BlogDetailSerializer,
)

# importing model
from .models import Blog


class BlogListAPI(generics.ListAPIView):
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,]
    search_fields = [
        'title',
        'content',
    ]
    pagination_class = BlogPageNumberPagination

    def get_queryset(self):
        qs = Blog.get_published_blogs.filter(~Q(status='PR'))
        query = self.request.GET.get("q") # getting query

        if query and query == "featured-blogs":
            qs = Blog.get_featured_blogs.filter(~Q(status='PR'))[:15]

        if query and query == "my-projects":
            qs = Blog.get_published_blogs.filter(status='P')[:6]

        return qs

class BlogDetailAPI(generics.RetrieveAPIView):
    serializer_class = BlogDetailSerializer
    lookup_field = "title_slug"

    def get_queryset(self):
        return Blog.get_published_blogs.all()