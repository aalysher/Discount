# Generated by Django 3.2.5 on 2021-08-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210803_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='discount_deadline',
            new_name='deadline',
        ),
        migrations.AlterField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[('1', 'Активирован'), ('2', 'Неактивирован'), ('3', 'Просрочен')], default='2', max_length=255, verbose_name='Статус операции'),
        ),
    ]
