# Generated by Django 4.2.16 on 2024-11-11 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='planned_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
