# Generated by Django 4.1.7 on 2023-06-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_view', '0012_alter_promotion_end_date_alter_promotion_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]