# Generated by Django 2.2.5 on 2019-09-13 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter_id', models.IntegerField()),
                ('reciver_id', models.IntegerField()),
                ('message_text', models.TextField(max_length=3000)),
                ('send_date', models.DateTimeField(default=datetime.datetime(2019, 9, 13, 20, 35, 39, 581232))),
            ],
        ),
    ]
