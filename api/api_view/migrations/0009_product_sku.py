# Generated by Django 4.1.7 on 2023-06-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0008_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.IntegerField(null=True),
        ),
    ]
