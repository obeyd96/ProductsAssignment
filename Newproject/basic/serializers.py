from rest_framework import serializers
from .models import Product, ProductColour, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    colour = serializers.PrimaryKeyRelatedField(
        read_only=True, source='productcolour.colour')
    image = serializers.PrimaryKeyRelatedField(
        read_only=True, source='productimage.image')

    class Meta:
        model = Product
        fields = ('title', 'description', 'price',
                  'unique_code', 'size', 'quality', 'colour', 'image')


class ProductColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColour
        fields = ('product', 'colour')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('product', 'image')
