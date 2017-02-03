from django.utils.encoding import force_text
from rest_framework import serializers

from .models import Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer"""

    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    """SubCategory Serializer"""

    class Meta:
        model = SubCategory
        fields = '__all__'
