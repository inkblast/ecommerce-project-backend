# Generated by Django 4.1.7 on 2023-06-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0006_remove_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
