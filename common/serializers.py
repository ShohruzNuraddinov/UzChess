from rest_framework import serializers

from .models import Contact, ContactInfo


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'phone_number', 'message', 'is_accepted', 'created_at']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'work_time', 'phone_number', 'email', 'metro', 'created_at']
