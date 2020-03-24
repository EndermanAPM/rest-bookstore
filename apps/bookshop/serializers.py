from django.db.transaction import atomic
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


class OrderBookQuantitySerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = OrderBookQuantity
        fields = "__all__"

class OrderSerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = Order
        fields = "__all__"

    @atomic
    def create(self, validated_data):
        super()
        order = Order.objects.create(**validated_data)
        customer = Customer.objects.get(pk=order.customer_id)
        customer.fidelity_points += 1
        customer.save()
        return order

class OrderDetailSerializer(HyperlinkedModelSerializerWithId):

    class OrderlessOrderBookQuantitySerializer(HyperlinkedModelSerializerWithId):
        class Meta:
            model = OrderBookQuantity
            exclude = ("order",)

    purchased_books = OrderlessOrderBookQuantitySerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
