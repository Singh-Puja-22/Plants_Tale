# Generated by Django 5.0.5 on 2024-05-06 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_plant_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='blooming_period',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='plant',
            name='care_tips',
            field=models.TextField(default='Not Available'),
        ),
        migrations.AddField(
            model_name='plant',
            name='description',
            field=models.TextField(default='Not Available'),
        ),
        migrations.AddField(
            model_name='plant',
            name='flower_color',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='plant',
            name='fragrance',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='plant',
            name='height',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='plant',
            name='scientific_name',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='plant',
            name='sunlight_requirements',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='plant',
            name='watering_needs',
            field=models.CharField(default='Not Available', max_length=100),
        ),
    ]