from .models import Item
from rest_framework import generics, filters
from .serializers import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ItemList(generics.ListAPIView):
    # Get all posts, limit = 20
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'price']
