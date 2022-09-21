from django.core.paginator import Paginator
from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import *
from .models import *


class ProductView(generics.CreateAPIView):
    queryset = Product
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):

        products = Product.objects.all()

        products = products.order_by('like')[::-1]

        product_serializer = self.serializer_class(instance=products, many=True)

        paginator = Paginator(product_serializer.data, 10)

        res = paginator.page(page)

        return Response(data=res.object_list, status=status.HTTP_200_OK)

    def post(self, request, page):

        data = request.data

        products = Product.objects.all()

        if data['type']:
            products = products.filter(type=data['type']).values()

        if data['category']:
            products = products.filter(category=data['category']).values()

        if data['size']:
            products = products.filter(size=data['size']).values()

        if data['color']:
            products = products.filter(color=data['color']).values()

        if data['price']:
            products = products.filter(price=data['price']).values()

        paginator = Paginator(products, 10)

        res = paginator.page(page)

        return Response(data=res.object_list, status=status.HTTP_200_OK)


class CategoryView(generics.CreateAPIView):
    queryset = Category
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category
    serializer_class = CategorySerializer


class TypeView(generics.CreateAPIView):
    queryset = Type
    serializer_class = TypeSerializer


class TypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type
    serializer_class = TypeSerializer
