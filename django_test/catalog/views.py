from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import filters as drf_filters
from .serializers import TagSerializer, GoodSerializer, CategorySerializer
from .models import Tag, Good, Category
from rest_framework.permissions import IsAuthenticated
from .filters import GoodsFilter

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GoodViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Good.objects.filter(active=True)
    serializer_class = GoodSerializer
    filter_backends = (filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter)
    ordering_fields = ['name', 'price']
    search_fields = ['name', 'description']
    filterset_class = GoodsFilter


class CategoryViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Category.objects.all().prefetch_related('goods')
    serializer_class = CategorySerializer
