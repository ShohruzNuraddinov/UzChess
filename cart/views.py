from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.db import models

from .serializers import CartItemCreateSerializer, CartItemgetSerializer
from .models import CartItem

# Create your views here.


class CreateCartItemView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerializer


class CartItemListView(generics.ListAPIView):
    queryset = CartItem.objects.annotate(
        sum=models.Sum('course__price') * models.F('quantity'),
        sum_book=models.Sum('book__price') * models.F('quantity')
    )
    serializer_class = CartItemgetSerializer
