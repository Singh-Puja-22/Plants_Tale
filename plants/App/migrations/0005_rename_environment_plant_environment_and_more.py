# Generated by Django 5.0.5 on 2024-05-15 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_plant_environment_plant_family_plant_landscape_use_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='Environment',
            new_name='environment',
        ),
        migrations.RenameField(
            model_name='plant',
            old_name='height',
            new_name='size',
        ),
    ]
