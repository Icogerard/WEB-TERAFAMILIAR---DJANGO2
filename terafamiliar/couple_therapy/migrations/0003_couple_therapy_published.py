# Generated by Django 2.1.2 on 2018-11-30 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('couple_therapy', '0002_auto_20181128_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='couple_therapy',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
        ),
    ]
