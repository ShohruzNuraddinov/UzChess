from rest_framework import serializers


from .models import CartItem
from course.serializers import CourseSerializera
from library.serializers import BookSerializer


class CartItemCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'user',
            'course',
            'book',
            'quantity'
        ]


class CartItemgetSerailizer(serializers.ModelSerializer):
    course = CourseSerializera()
    book = BookSerializer()
    sum = serializers.FloatField()
    sum_book = serializers.FloatField()

    class Meta:
        model = CartItem
        fields = [
            'user',
            'course',
            'book',
            'quantity',
            'sum',
            'sum_book'
        ]
