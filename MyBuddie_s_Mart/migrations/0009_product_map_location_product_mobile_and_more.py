# Generated by Django 5.0.3 on 2024-03-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBuddie_s_Mart', '0008_remove_product_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='map_location',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mobile',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='telephone',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]