# Generated by Django 3.2.6 on 2022-04-13 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('map', '0004_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='date happened')),
                ('event', models.CharField(max_length=200)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='map.place')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
