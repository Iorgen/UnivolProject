# Generated by Django 2.2.5 on 2019-09-14 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univol', '0009_auto_20190914_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='date_range',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 4, 19, 0, 659581)),
        ),
    ]
