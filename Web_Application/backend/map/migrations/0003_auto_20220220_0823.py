# Generated by Django 3.2.6 on 2022-02-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_place_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='genres',
            field=models.ManyToManyField(related_name='places', to='map.Genre'),
        ),
    ]