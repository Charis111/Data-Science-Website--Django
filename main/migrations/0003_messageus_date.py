# Generated by Django 3.0.4 on 2020-04-25 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200425_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 22, 4, 11, 363818), verbose_name='date sent'),
        ),
    ]