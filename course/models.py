from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Category')
    cours_count = models.IntegerField()


class Course(models.Model):
    Degre = (
        ('boshlangich', 'Boshlangich'),
        ('profesional', 'Profesional'),
        ('havaskor', 'Havaskor'),
    )
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Course')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, choices=Degre)

    rating = models.FloatField()

    section_count = models.IntegerField()
    lesson_count = models.IntegerField()
    comment_count = models.IntegerField()


class Lesson(models.Model):
    cours = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='Lesson')


class Comment(models.Model):
    user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.IntegerField()


class Complaint(models.Model):
    demo = (
        ('yomon_mavzu', 'Yomon mavzu'),
        ('yomon_ustoz', 'Yomon ustoz'),
        ('yomon_sayt', 'Yomon sayt'),
    )
    user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    cours = models.ForeignKey(Course, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=50, choices=demo)
    text = models.CharField(max_length=300)
