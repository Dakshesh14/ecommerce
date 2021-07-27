from rest_framework import serializers

# importing model
from .models import (
    Item,
    ItemImage,
    Category,
    Cart,
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
    thumbnail = serializers.ImageField(source="get_first_thumbnail_img")

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'content',
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
            'title_slug',
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
            'title_slug',
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


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'item',
            'quantity',
        )

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = (
            'image',
        )
