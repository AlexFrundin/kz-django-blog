# Generated by Django 3.1.3 on 2021-01-22 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movie_lenth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='lenth',
        ),
    ]
