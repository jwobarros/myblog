# Generated by Django 3.0.1 on 2019-12-28 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]