# Generated by Django 4.0.2 on 2022-09-11 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_alter_item_created_on_alter_orders_placed_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 11, 12, 31, 23, 257164)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='placed_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 11, 12, 31, 23, 258175)),
        ),
    ]
