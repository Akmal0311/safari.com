from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
