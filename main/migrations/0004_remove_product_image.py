# Generated by Django 5.0 on 2023-12-29 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_image_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
