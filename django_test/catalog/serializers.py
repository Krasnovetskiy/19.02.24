from rest_framework import serializers
from .models import Tag, Good


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'uuid']


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'description', 'price', 'active', ]
