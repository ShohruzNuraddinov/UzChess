from django.db import models

from utils.models import BaseModel
from user.models import CustomUser as User
from course.models import Course
from library.models import Book

# Create your models here.


class CartItem(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.user.id) + ' ' + str(self.quantity)
