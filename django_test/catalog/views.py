from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TagSerializer, GoodSerializer, CategorySerializer
from .models import Tag, Good, Category


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.filter(active=True)
    serializer_class = GoodSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
