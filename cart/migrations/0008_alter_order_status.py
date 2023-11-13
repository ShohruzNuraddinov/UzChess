# Generated by Django 4.2.7 on 2023-11-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=50),
        ),
    ]