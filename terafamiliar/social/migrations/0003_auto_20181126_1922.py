# Generated by Django 2.1.2 on 2018-11-27 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20181126_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='ulr',
            new_name='url',
        ),
    ]
