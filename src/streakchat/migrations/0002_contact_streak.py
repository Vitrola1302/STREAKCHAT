# Generated by Django 4.2.1 on 2023-06-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streakchat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='streak',
            field=models.IntegerField(default=0),
        ),
    ]
