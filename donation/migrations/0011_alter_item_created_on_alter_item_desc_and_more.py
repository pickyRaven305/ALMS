# Generated by Django 4.0.2 on 2022-09-11 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0010_alter_item_created_on_alter_item_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 11, 21, 0, 27, 797979)),
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='static/images/NA_img.svg', upload_to='login/images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='orders',
            name='placed_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 11, 21, 0, 27, 797979)),
        ),
    ]