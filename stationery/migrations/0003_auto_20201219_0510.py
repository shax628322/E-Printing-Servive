# Generated by Django 3.1.4 on 2020-12-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0002_remove_stationery_stationery_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationery',
            name='Stationery_slug',
            field=models.TextField(max_length=200),
        ),
    ]
