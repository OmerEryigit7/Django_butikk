# Generated by Django 5.1 on 2025-05-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('butikk_app', '0002_productinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='image',
            field=models.ImageField(upload_to='butikk_app/static/images'),
        ),
    ]
