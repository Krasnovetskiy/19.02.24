from django.db.models import Count
from rest_framework import serializers
from .models import Tag, Good, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'uuid']


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'description', 'price', 'active']


class CategorySerializer(serializers.ModelSerializer):
    goods = GoodSerializer(many=True, read_only=True)
    good_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'goods', 'good_count']

    def get_good_count(self, Category):
        count = Category.goods.count()
        return count
