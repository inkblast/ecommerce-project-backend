# Generated by Django 4.1.7 on 2023-06-08 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0005_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
