# Generated by Django 4.2.3 on 2024-11-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0002_rooms"),
    ]

    operations = [
        migrations.AddField(
            model_name="rooms",
            name="imagen",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="rooms",
            name="imagen_2",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
