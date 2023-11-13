from django.urls import path, include

from .views import (
    ContactListCreateAPIView,
    ContactDetailAPIView,
    ContactInfoRetrieveAPIView,
)
urlpatterns = [
    path('', ContactListCreateAPIView.as_view(), name='contact'),
    path('<int:pk>/', ContactDetailAPIView.as_view(), name='contact-detail'),
    path('info/', ContactInfoRetrieveAPIView.as_view(), name='contact-retrieve'),
]
