# Generated by Django 4.2.5 on 2023-10-29 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0004_alter_cruise_destinations_inforequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='slug',
        ),
    ]
