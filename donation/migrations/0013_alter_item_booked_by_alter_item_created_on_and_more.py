# Generated by Django 4.0.2 on 2022-09-11 21:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donation', '0012_alter_item_booked_by_alter_item_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='booked_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 11, 21, 16, 29, 976487)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='placed_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 11, 21, 16, 29, 977485)),
        ),
    ]
