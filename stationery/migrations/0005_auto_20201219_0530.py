# Generated by Django 3.1.4 on 2020-12-19 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0004_auto_20201219_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationery',
            name='Stationery_service_offer',
        ),
        migrations.AddField(
            model_name='stationery',
            name='Group_Task',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stationery',
            name='Individual_Task',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stationery',
            name='Paper',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stationery',
            name='Report',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stationery',
            name='Research',
            field=models.BooleanField(default=False),
        ),
    ]
