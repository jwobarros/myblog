# Generated by Django 3.0.1 on 2020-01-10 20:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200110_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=ckeditor.fields.RichTextField(verbose_name='Resumo'),
        ),
    ]
