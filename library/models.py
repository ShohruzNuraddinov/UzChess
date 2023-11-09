from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from utils.models import BaseModel


class DegreeChoice(models.TextChoices):
    amateur = "Havaskor"
    initial = "Boshlang'ich"
    professional = "Professional"


class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class BookCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Book(BaseModel):
    # relations
    category = models.ForeignKey(
        BookCategory, on_delete=models.CASCADE, related_name='books'
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author_books'
    )

    # choice fields
    degree = models.CharField(
        max_length=20, choices=DegreeChoice.choices, default=DegreeChoice.initial
    )

    # fields
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images/')
    content = RichTextUploadingField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    old_price = models.DecimalField(max_digits=20, decimal_places=2)
    number_of_pages = models.IntegerField()
    is_top = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} - {self.title}"
