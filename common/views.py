from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .models import Contact, ContactInfo
from .serializers import ContactSerializer, ContactInfoSerializer


class ContactListCreateAPIView(ListCreateAPIView):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer


class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoRetrieveAPIView(ListCreateAPIView):
    queryset = ContactInfo.objects.all()[:1]
    serializer_class = ContactInfoSerializer
