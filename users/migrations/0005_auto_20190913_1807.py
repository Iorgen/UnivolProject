# Generated by Django 2.2.5 on 2019-09-13 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190913_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='county',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='organizator',
            name='Logo',
        ),
        migrations.RemoveField(
            model_name='organizator',
            name='address',
        ),
        migrations.RemoveField(
            model_name='organizator',
            name='city',
        ),
        migrations.RemoveField(
            model_name='organizator',
            name='country',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='User photo',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='employment_situation',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='rating',
        ),
    ]
