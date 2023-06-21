from rest_framework.decorators import api_view
from rest_framework.response import Response
from CrawlingAPI.models import Product
from CrawlingAPI.serializers.product import ProductSerializer

@api_view(['GET'])
def get_products(_):
    #Here we're gonna get all the objects in the database and send them to the api
    #We need to serialize the objects to tranform the queryset into real objects
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True)
    return Response({"products": data.data})