from rest_framework import serializers

# importing model
from .models import (
    Item,
    ItemImage,
    Category,
)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'ct',
        )


class ItemListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.ct")
    detail = serializers.HyperlinkedIdentityField(
        view_name='item-detail',
        lookup_field="title_slug"
    )
    thumbnail = serializers.ImageField(source="get_first_thumbnail_img")

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'content',
            'detail',
            'price',
            'title_slug',
            'category',
            'thumbnail',
        )


class FeaturedProductSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(source="get_first_thumbnail_img")

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'thumbnail',
            'price',
        )


class ItemDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.ct")
    status = serializers.CharField(source='get_status_display')
    images = serializers.SerializerMethodField()
    featured_products = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            'title',
            'content',
            'price',
            'status',
            'category',
            'featured_products',
            'images',
        )

    def get_featured_products(self, obj):
        qs = Item.get_featured_product.all()
        serializered_children = FeaturedProductSerializer(qs, many=True)
        return serializered_children.data

    def get_images(self, obj):
        children = obj.get_product_image()
        serializered_children = ItemImageSerializer(children, many=True)
        return serializered_children.data


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = (
            'image',
        )
