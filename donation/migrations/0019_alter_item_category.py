# Generated by Django 4.0.2 on 2022-09-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0018_alter_donate_donated_on_alter_item_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('food', 'FOOD'), ('clothing', 'CLOTHING'), ('clothing', 'CLOTHING'), ('utensils', 'UTENSILS'), ('Others', 'OTHERS')], default='clothing', max_length=30),
        ),
    ]