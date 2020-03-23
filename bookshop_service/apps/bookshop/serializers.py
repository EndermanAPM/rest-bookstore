from drf_nested_serializer import NestedModelSerializer
from rest_framework import serializers
from .models import *


class HyperlinkedModelSerializerWithId(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)


class CustomerSerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = Customer
        fields = "__all__"


class GenreSerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = Book
        fields = "__all__"


class OrderBookSerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = OrderBook
        fields = "__all__"
        # exclude = ("order", )

class OrderlessOrderBookSerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = OrderBook
        exclude = ("order", )

class OrderSerializer(HyperlinkedModelSerializerWithId):
    purchased_books = OrderlessOrderBookSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        validated_purchased_books = validated_data.pop('purchased_books')
        order = Order.objects.create(**validated_data)
        book_serializer = self.fields['purchased_books']
        for each in validated_purchased_books:
            each['order'] = order
        choices = book_serializer.create(validated_purchased_books)

        customer = Customer.objects.get(pk=order.customer_id)
        customer.fidelity_points += 1
        customer.save()
        return order

