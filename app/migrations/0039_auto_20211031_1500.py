# Generated by Django 2.2.8 on 2021-10-31 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20210929_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='profilestatus',
            field=models.CharField(blank=True, default='PREMIUM', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='renewal_date',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
