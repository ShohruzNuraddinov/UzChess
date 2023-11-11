from django.db import models
from django.contrib.auth import get_user_model

from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver
from hitcount.models import HitCount

from utils.models import BaseModel

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class New(BaseModel):
    # relations
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='news')

    # fields
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    content = RichTextUploadingField()
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title
