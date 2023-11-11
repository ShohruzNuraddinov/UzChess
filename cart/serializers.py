from rest_framework import serializers


from .models import CartItem
from course.serializers import CourseSerializera
from library.serializers import BookSerializer
from user.models import CustomUser as User


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'user',
            'course',
            'book',
            'quantity'
        ]


class CartItemgetSerializer(serializers.ModelSerializer):
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


class UserCartItemGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
