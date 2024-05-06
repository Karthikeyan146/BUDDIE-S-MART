# Generated by Django 5.0.3 on 2024-03-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBuddie_s_Mart', '0009_product_map_location_product_mobile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='map_location',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='product',
            name='telephone',
        ),
        migrations.AddField(
            model_name='shop',
            name='map_location',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='mobile',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='telephone',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]