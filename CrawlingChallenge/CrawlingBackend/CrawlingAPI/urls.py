from django.urls import path

from CrawlingAPI.views import products_view as main_views

urlpatterns = [
    path('api/products', main_views.get_products, name='api-products')
]
