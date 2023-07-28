# Generated by Django 4.2.1 on 2023-06-15 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivered',
            fields=[
                ('codesKey', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_quentity', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('cust_name', models.CharField(max_length=100)),
                ('cust_email', models.CharField(max_length=100)),
                ('cust_address', models.CharField(max_length=100)),
                ('cust_phone', models.CharField(max_length=10)),
                ('date_created', models.CharField(max_length=10)),
                ('order_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Order',
            fields=[
                ('codesKey', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_quentity', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('cust_name', models.CharField(max_length=100)),
                ('cust_email', models.CharField(max_length=100)),
                ('cust_address', models.CharField(max_length=100)),
                ('cust_phone', models.CharField(max_length=10)),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('order_status', models.CharField(max_length=100)),
            ],
        ),
    ]
