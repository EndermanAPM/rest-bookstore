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

class OrderBookSummarySerializer(HyperlinkedModelSerializerWithId):
    class Meta:
        model = OrderBook
        exclude = ("order", )

class OrderSerializer(HyperlinkedModelSerializerWithId):
    purchased_books = OrderBookSummarySerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        choice_validated_data = validated_data.pop('purchased_books')
        order = Order.objects.create(**validated_data)
        choice_set_serializer = self.fields['purchased_books']
        for each in choice_validated_data:
            each['order'] = order
        choices = choice_set_serializer.create(choice_validated_data)
        return order