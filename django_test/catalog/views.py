from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TagSerializer, GoodSerializer, CategorySerializer
from .models import Tag, Good, Category
from rest_framework.permissions import IsAuthenticated


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.filter(active=True)
    serializer_class = GoodSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all().prefetch_related('goods')
    serializer_class = CategorySerializer
