from rest_framework import serializers

# importing model
from .models import (
    Item,
)


class ItemListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.ct")
    detail = serializers.HyperlinkedIdentityField(
        view_name='item-detail',
        lookup_field="title_slug"
    )

    class Meta:
        model = Item
        fields = (
            'title',
            'content',
            'detail',
            'price',
            'title_slug',
            'category',
        )


class ItemDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.ct")
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Item
        fields = (
            'title',
            'content',
            'category',
            'price',
            'status',
        )
