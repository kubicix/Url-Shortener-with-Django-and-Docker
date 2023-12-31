# Generated by Django 4.1.3 on 2023-10-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortenedurl',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='original_url',
            field=models.URLField(max_length=2048, unique=True),
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_url',
            field=models.CharField(max_length=22, unique=True),
        ),
    ]
