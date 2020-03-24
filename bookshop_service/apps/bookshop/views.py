from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .serializers import *


class OrderModelViewSet(viewsets.ModelViewSet):
    ordering_fields = ['id']
    ordering = ['-id']
    search_fields = ['id']


class CustomerAPI(OrderModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    search_fields = ['id', 'name']



class GenreAPI(OrderModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    search_fields = ['id', 'name']



class BookAPI(OrderModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    search_fields = ['id', 'name']



class OrderAPI(OrderModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filterset_fields = ['status']
    detail_serializer_class = OrderDetailSerializer

    def get_serializer_class(self):
        """
        Determins which serializer to user `list` or `detail`
        """
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return super().get_serializer_class()


class OrderBookQuantityAPI(OrderModelViewSet):
    serializer_class = OrderBookQuantitySerializer
    queryset = OrderBookQuantity.objects.all()


# ReadOnlyModelViewSet
