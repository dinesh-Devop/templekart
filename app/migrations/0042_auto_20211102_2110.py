# Generated by Django 2.2.8 on 2021-11-02 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_remove_pointstable_tournament'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointstable',
            name='draw',
        ),
        migrations.RemoveField(
            model_name='pointstable',
            name='lose',
        ),
        migrations.RemoveField(
            model_name='pointstable',
            name='teams',
        ),
    ]
