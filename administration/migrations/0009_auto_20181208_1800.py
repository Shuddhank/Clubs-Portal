# Generated by Django 2.1.2 on 2018-12-08 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0008_auto_20181208_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onpollclub',
            name='release_date',
            field=models.TimeField(default=datetime.datetime(2018, 12, 8, 18, 0, 26, 369857)),
        ),
    ]
