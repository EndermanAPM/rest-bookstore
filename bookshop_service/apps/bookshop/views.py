from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *


class CustomerAPI(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class GenreAPI(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class BookAPI(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class OrderAPI(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderBookQuantityAPI(viewsets.ModelViewSet):
    serializer_class = OrderBookQuantitySerializer
    queryset = OrderBookQuantity.objects.all()

