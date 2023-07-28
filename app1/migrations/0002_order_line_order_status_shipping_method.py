# Generated by Django 4.2.1 on 2023-07-10 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_line',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customize_product_id', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order_status',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_method',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]