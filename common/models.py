from django.db import models

from utils.models import BaseModel


class Contact(BaseModel):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class ContactInfo(BaseModel):
    work_time = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    metro = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.email
