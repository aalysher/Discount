# Generated by Django 3.2.5 on 2021-08-05 04:58

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_discount_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='pin',
            field=models.CharField(default=core.models.get_random_pin, max_length=4, verbose_name='Пин-код'),
        ),
    ]
