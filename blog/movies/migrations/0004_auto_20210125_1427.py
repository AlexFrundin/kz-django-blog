# Generated by Django 3.1.3 on 2021-01-25 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('movies', '0003_auto_20210125_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='object_id',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
