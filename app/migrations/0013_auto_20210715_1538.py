# Generated by Django 2.2.8 on 2021-07-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
