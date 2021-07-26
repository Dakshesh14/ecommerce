from rest_framework import serializers

# importing model 
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):

    thumbnail_small = serializers.ImageField(read_only=True)
    date_added = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'about',
            'title_slug',
            'date_added',
            'thumbnail_small',
        )

    def get_date_added(self, obj):
        return f"{obj.date_added.strftime('%d %b %Y')}"


class BlogDetailSerializer(serializers.ModelSerializer):

    date_added = serializers.SerializerMethodField()
    last_edited = serializers.SerializerMethodField()
    related_blogs = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.ct")

    class Meta:
        model = Blog
        fields = (
            'title',
            'content',
            'category',
            'keywords',
            'thumbnail',
            'date_added',
            'last_edited',
            'related_blogs',
        )

    def get_related_blogs(self, obj):
        if obj and obj.category:
            qs = Blog.objects.filter(category=obj.category).exclude(id=obj.id)[:5]
            return BlogSerializer(qs, many=True).data
        
        return None


    def get_date_added(self, obj):
        return f"{obj.date_added.strftime('%d %b %Y')}"

    def get_last_edited(self, obj):
        return f"{obj.last_edited.strftime('%d %b %Y')}"