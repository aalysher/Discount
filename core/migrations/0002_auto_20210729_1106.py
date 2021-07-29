# Generated by Django 3.2.5 on 2021-07-29 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='instruction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instruction'),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city'),
        ),
        migrations.AlterField(
            model_name='location',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
        migrations.AlterField(
            model_name='view',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.company', unique=True),
        ),
    ]
