# Generated by Django 4.1.7 on 2023-06-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0007_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
