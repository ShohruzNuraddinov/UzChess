from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.db import models

from .serializers import CartItemCreateSerailizer, CartItemgetSerailizer
from .models import CartItem

# Create your views here.


class CreateCartItemView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerailizer


class CartItemListView(generics.ListAPIView):
    queryset = CartItem.objects.annotate(
        sum=models.Sum('course__price') * models.F('quantity'),
        sum_book=models.Sum('book__price') * models.F('quantity')
    )
    serializer_class = CartItemgetSerailizer
