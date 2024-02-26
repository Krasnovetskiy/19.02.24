from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TagSerializer, GoodSerializer
from .models import Tag, Good


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.filter(active=True)
    serializer_class = GoodSerializer
