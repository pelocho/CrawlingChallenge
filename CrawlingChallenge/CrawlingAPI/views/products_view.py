from rest_framework.decorators import api_view
from rest_framework.response import Response
from CrawlingAPI.models import Product
from CrawlingAPI.serializers.product import ProductSerializer

@api_view(['GET'])
def get_products(_):
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True)
    return Response({"products": data.data})