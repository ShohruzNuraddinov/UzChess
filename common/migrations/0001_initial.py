# Generated by Django 4.2.7 on 2023-11-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('work_time', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('metro', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
