# Generated by Django 3.2 on 2021-04-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='p_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
