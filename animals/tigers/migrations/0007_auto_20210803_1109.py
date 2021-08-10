# Generated by Django 3.2.4 on 2021-08-03 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tigers', '0006_alter_photos_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='anons',
        ),
        migrations.RemoveField(
            model_name='news',
            name='main_photo',
        ),
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.CharField(default=django.utils.timezone.now, max_length=250, verbose_name='Главное фото'),
            preserve_default=False,
        ),
    ]