# Generated by Django 2.1.2 on 2018-11-27 19:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individual_therapy', '0002_auto_20181121_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual_therapy',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
