from django.urls import path

from .views import CreateCartItemView, CartItemListView

urlpatterns = [
    path('', CartItemListView.as_view()),
    path('add/', CreateCartItemView.as_view()),
]
