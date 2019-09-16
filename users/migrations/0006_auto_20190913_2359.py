# Generated by Django 2.2.5 on 2019-09-13 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190913_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='usr', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]