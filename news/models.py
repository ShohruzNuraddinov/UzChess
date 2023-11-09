from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from utils.models import BaseModel


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class New(BaseModel):
    # relations
    tag = models.ManyToManyField(Tag)

    # fields
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    content = RichTextUploadingField()
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title
