# Generated by Django 5.0.3 on 2024-03-11 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyBuddie_s_Mart', '0007_alter_product_name_alter_shop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='address',
        ),
    ]
