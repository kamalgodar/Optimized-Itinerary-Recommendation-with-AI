# Generated by Django 3.2.6 on 2022-04-13 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_alter_log_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date happened'),
        ),
    ]
