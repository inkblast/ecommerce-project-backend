# Generated by Django 4.1.7 on 2023-06-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0003_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(max_length=300, null=True, upload_to='image/%y/%m/%d/'),
        ),
    ]
