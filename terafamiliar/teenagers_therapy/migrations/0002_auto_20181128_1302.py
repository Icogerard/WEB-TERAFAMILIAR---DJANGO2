# Generated by Django 2.1.2 on 2018-11-28 19:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teenagers_therapy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teenagers_therapy',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
