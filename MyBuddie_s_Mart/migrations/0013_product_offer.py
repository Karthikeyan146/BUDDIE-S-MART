# Generated by Django 5.0.3 on 2024-03-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBuddie_s_Mart', '0012_product_current_price_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.IntegerField(default=0),
        ),
    ]
