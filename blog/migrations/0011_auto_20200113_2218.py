# Generated by Django 3.0.1 on 2020-01-14 02:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200110_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True),
        ),
    ]
