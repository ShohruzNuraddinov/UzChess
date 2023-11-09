# Generated by Django 4.2.7 on 2023-11-09 11:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='news_images/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('view', models.IntegerField(default=0)),
                ('tag', models.ManyToManyField(to='news.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
