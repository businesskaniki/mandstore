# Generated by Django 3.2 on 2021-04-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_products_p_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='p_price',
            field=models.TextField(null=True),
        ),
    ]