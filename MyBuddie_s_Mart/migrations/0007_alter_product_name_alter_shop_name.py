# Generated by Django 5.0.3 on 2024-03-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBuddie_s_Mart', '0006_alter_product_name_alter_shop_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
