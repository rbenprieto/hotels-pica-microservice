# Generated by Django 4.2.3 on 2024-11-10 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("availability", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentsreservations",
            name="reserva",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="availability.reservations",
            ),
        ),
    ]