# Generated by Django 4.0.2 on 2022-09-10 17:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('food', 'FOOD'), ('clothing', 'CLOTHING'), ('Othhers', 'OTHERS')], default='clothing', max_length=30)),
                ('cost', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 10, 17, 19, 54, 860329))),
                ('image', models.ImageField(default='', upload_to='login/images')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_on', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 10, 17, 19, 54, 860329))),
                ('item_ordered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.item')),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
