# Generated by Django 2.1.2 on 2018-11-23 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_auto_20181123_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=200, null=True, verbose_name='Subtítulo'),
        ),
    ]
