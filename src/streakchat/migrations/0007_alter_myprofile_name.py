# Generated by Django 4.2.1 on 2023-06-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streakchat', '0006_alter_myprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
