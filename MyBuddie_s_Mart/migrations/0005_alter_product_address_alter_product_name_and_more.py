# Generated by Django 5.0.3 on 2024-03-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBuddie_s_Mart', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='address',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
