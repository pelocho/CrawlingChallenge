from rest_framework.serializers import ModelSerializer, StringRelatedField

from CrawlingAPI.models import Product

class ProductSerializer(ModelSerializer):
    availability = StringRelatedField(many=True)
    sizes = StringRelatedField(many=True)
    images_url = StringRelatedField(many=True)
    colors = StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'brand', 'description', 'current_price', 'original_price', 'category_path', 'availability', 'sizes', 'images_url', 'colors']
        